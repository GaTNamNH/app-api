from rest_framework import serializers
from .serializers import CategorySerializers
from .models import Category

class CategoryInDecorators(serializers.Serializer):
    display_name = serializers.CharField(max_length=50)