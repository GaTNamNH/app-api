from django.utils.decorators import method_decorator
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from url_filter.integrations.drf import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from .serializers import CategorySerializers
from .decorators import CategoryInDecorators
from .models import Category

# Create your views here.


@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_description="create post",
    request_body=CategoryInDecorators,
    responses={201: CategorySerializers}
))
@method_decorator(name='update', decorator=swagger_auto_schema(
    operation_description="update post",
    request_body=CategoryInDecorators,
    responses={205: CategorySerializers}
))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(
    operation_description="partial update post",
    request_body=CategoryInDecorators,
    responses={205: CategorySerializers}
))
class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'
    permission_classes = (IsAuthenticatedOrReadOnly, )
