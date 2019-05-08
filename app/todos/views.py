#from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK)
from drf_yasg.utils import swagger_auto_schema
from .serializers import TodoSerializers, CategorySerializers, TagSerializers
from .models import Todo, Category, Tag
from url_filter.integrations.drf import DjangoFilterBackend
# Create your views here.

class TodoViewset(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'

    @swagger_auto_schema(method='post', operation_description='GET /todos/today/')
    @action(detail=False, methods=['post'])
    def today(self, request):
        print(request.COOKIES)
        return Response({
            'status': False,
            'data': 'all'
        }, status=HTTP_200_OK)

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class TagViewset(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers