import regex
from collections import OrderedDict
from django.utils.decorators import method_decorator
from django.core.paginator import (
    Paginator, Page, EmptyPage, PageNotAnInteger
)
from rest_framework import viewsets, mixins, generics, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from url_filter.integrations.drf import DjangoFilterBackend
from elasticsearch_dsl.query import Q
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from utilities.permissions import DataMngPermission
from utilities.paging import StandardResultsSetPagination, ElasticSearchResults
from .serializers import CategorySerializers, PostSerializers
from .decorators import (CategoryInDecorators, PostOutDecorators, PostElasticMappingDecorators,
    PostListOutDecorators, PostInDecorators, PostPartialInDecorators)
from .models import Post, Category
# from .document import PostDocument

# Create your views here.

# _keywords = openapi.Parameter('q', openapi.IN_QUERY, type=openapi.TYPE_STRING, description='Search by free words')

# @method_decorator(name='list', decorator=swagger_auto_schema(
#     operation_description="get post list",
#     manual_parameters=[_keywords, ],
#     responses={200: PostListOutDecorators}
# ))
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
    queryset = Post.objects.filter(is_active=True)
    serializer_class = PostSerializers
    parser_classes = (MultiPartParser, )
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'
    permission_classes = (DataMngPermission, )
    pagination_class = StandardResultsSetPagination

    # def list(self, request, *args, **kwargs):
    #     _page = request.GET.get('page') if request.GET.get('page') else 1
    #     _page_size = request.GET.get('page_size') if request.GET.get('page_size') else 20
    #     _q = request.GET.get('q')

    #     must=[]

    #     if _q:
    #         keywords = regex.sub(u'[^\p{Latin}|[0-9]|\s*]', u' ', _q).split()
    #         for keyword in keywords:
    #             must.append(
    #                 Q('fuzzy', title=keyword) |
    #                 Q('fuzzy', intro=keyword) |
    #                 Q('nested', path='categories', query=Q('fuzzy', categories__display_name=keyword))
    #             )
    #     must.append(Q('match', is_active=True))

    #     s = PostDocument.search().query('bool', must=must).sort('-publish_time')
    #     results = ElasticSearchResults(s)

    #     paginator = Paginator(results, _page_size)
    #     try:
    #         response = paginator.page(_page)
    #     except PageNotAnInteger:
    #         response = paginator.page(1)
    #     except EmptyPage:
    #         response = paginator.page(paginator.num_pages)
    #     posts = PostElasticMappingDecorators(many=True, data=list(hit.to_dict() for hit in list(response)))
    #     posts.is_valid(raise_exception=True)
    #     return Response(OrderedDict([
    #         ('count', paginator.count),
    #         ('results', posts.data)
    #     ]), status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs)
        serializer.save(is_active=False)
        return Response(status=status.HTTP_204_NO_CONTENT)


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
    permission_classes = (DataMngPermission, )
