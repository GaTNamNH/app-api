#from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK)
from .serializers import TodoSerializers
from .models import Todo
# Create your views here.

class TodoViewset(viewsets.ModelViewSet):
    "abc ddef"

    queryset = Todo.objects.all()
    serializer_class = TodoSerializers

    @list_route()
    def list_all(self, request):
        "list all"

        return Response({
            'status': False,
            'data': 'all'
        }, status=HTTP_200_OK)
