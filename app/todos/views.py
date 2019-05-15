#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK)
from drf_yasg.utils import swagger_auto_schema
from .serializers import TodoSerializers, CategorySerializers, TagSerializers
from .models import Todo, Category, Tag
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework import permissions
from .document import TodoDocument
# Create your views here.

class TodoViewset(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    @action(detail=False, methods=['get', 'post'])
    def snippet_list(self, request):
        """
        List all code snippets, or create a new snippet.
        """
        if request.method == 'GET':
            tags = Tag.objects.all()
            serializer = TagSerializers(tags, many=True)
            return JsonResponse(serializer.data, safe=False)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = TagSerializers(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)

    @swagger_auto_schema(
        method='post',
        operation_description='GET /todos/elastic/',
        request_body=TagSerializers,
        responses={
            200: CategorySerializers,
            201: TagSerializers
        }
    )
    @action(detail=False, methods=['post'])
    def elastic(self, request):
        s = TodoDocument.search().query("fuzzy", subject="tring3")
        for hit in s:
            print("Todo >> subject: {}, content: {}".format(hit.subject, hit.content))
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