from django.utils.decorators import method_decorator
from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from url_filter.integrations.drf import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from .serializers import PostSerializers
from .decorators import (PostOutDecorators,
    PostInDecorators, PostPartialInDecorators)
from .models import Post


@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_description="create post",
    request_body=PostInDecorators,
    responses={201: PostOutDecorators}
))
@method_decorator(name='update', decorator=swagger_auto_schema(
    operation_description="update post",
    request_body=PostInDecorators,
    responses={205: PostOutDecorators}
))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(
    operation_description="partial update post",
    request_body=PostPartialInDecorators,
    responses={205: PostOutDecorators}
))
class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    parser_classes = (MultiPartParser, )
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'
    # permission_classes = (IsAuthenticatedOrReadOnly, )
