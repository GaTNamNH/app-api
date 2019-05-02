#from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK)
from drf_yasg.utils import swagger_auto_schema
from .serializers import TodoSerializers
from .models import Todo
# Create your views here.

class TodoViewset(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers

    @swagger_auto_schema(method='post', operation_description='GET /articles/today/')
    @action(detail=False, methods=['post'])
    def today(self, request):
        return Response({
            'status': False,
            'data': 'all'
        }, status=HTTP_200_OK)