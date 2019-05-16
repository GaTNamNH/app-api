# Create your views here.
from datetime import datetime
from django.http import HttpResponse, Http404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from requests import HTTPError
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_social_auth.serializers import JWTSerializer
from rest_social_auth.views import decorate_request
from social_core.exceptions import AuthException
from rest_framework.exceptions import APIException
from social_core.utils import parse_qs
from .serializers import OAuth2TokenInputSerializer
from rest_social_auth.views import SocialJWTOnlyAuthView

class SocialAuthenticationView:
    param = openapi.Parameter('var', openapi.IN_PATH,
                              description="provider of social account. for web app: facebook-token, for ios and android app: facebook-app",
                              type=openapi.TYPE_STRING)
    @method_decorator(name='post', decorator=swagger_auto_schema(
        operation_summary='Login with social account',
        operation_description='Get JWT using social account access token',
        manual_parameters=[param],
        request_body=OAuth2TokenInputSerializer,
        responses={200: JWTSerializer}
    ))
    class SocialAuthenticationViewSet(SocialJWTOnlyAuthView):
        oauth2_serializer_class_in = OAuth2TokenInputSerializer
        @method_decorator(never_cache)
        def post(self, request, *args, **kwargs):
            input_data = self.get_serializer_in_data()
            provider_name = self.get_provider_name(input_data)
            if not provider_name:
                return self.respond_error("Provider is not specified")
            self.set_input_data(request, input_data)
            decorate_request(request, provider_name)
            serializer_in = self.get_serializer_in(data=input_data)
            if self.oauth_v1() and request.backend.OAUTH_TOKEN_PARAMETER_NAME not in input_data:
                # oauth1 first stage (1st is get request_token, 2nd is get access_token)
                request_token = parse_qs(request.backend.set_unauthorized_token())
                return Response(request_token)
            serializer_in.is_valid(raise_exception=True)
            try:
                user = self.get_object()
            except (AuthException, HTTPError) as e:
                return self.respond_error(e)
            if isinstance(user, HttpResponse):  # An error happened and pipeline returned HttpResponse instead of user
                return user
            resp_data = self.get_serializer(instance=user)
            print(resp_data)
            self.do_login(request.backend, user)
            return Response(resp_data.data)

