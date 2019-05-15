#from django.shortcuts import render
from rest_framework import viewsets
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED)
from drf_yasg.utils import swagger_auto_schema
from .serializers import PostSerializers, PostInputSerializers
from .models import Post
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.parsers import (FormParser, MultiPartParser)
# Create your views here.

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'
    parser_classes = (MultiPartParser, )
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    @swagger_auto_schema(
        operation_description='POST /post/boto/',
        request_body=PostInputSerializers,
        responses={
            201: PostSerializers
        }
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=HTTP_201_CREATED, headers=headers)

    # @swagger_auto_schema(
    #     method='post',
    #     operation_description='POST /post/boto/'
    # )
    # @action(detail=False, methods=['post'])
    # def boto(self, request):
        
    #     for bucket in s3.buckets.all():
    #         print(bucket.name)
    #     return Response({
    #         'status': False,
    #         'data': 'all'
    #     }, status=HTTP_200_OK)
