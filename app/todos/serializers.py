from rest_framework import serializers
from .models import Todo, Category, Tag

class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title')

class TagSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'title')

class TodoSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    subject = serializers.CharField()
    content = serializers.CharField()
    timer = serializers.TimeField()
    created = serializers.DateTimeField(read_only=True)
    # category = serializers.PKOnlyObject(pk=True)
    category = CategorySerializers()
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Todo
        fields = '__all__'
