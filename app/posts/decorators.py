from rest_framework import serializers
from users.decorators import UserBasicDecorators
from job.serializers import MajorSerializers
from .serializers import CategorySerializers, PostSerializers
from .models import Category, Post, POST_STATE

class CategoryInDecorators(serializers.Serializer):
    display_name = serializers.CharField(max_length=50)

class PostOutDecorators(PostSerializers):
    """
    decorator class
    """
    categories = CategorySerializers(many=True, read_only=True)
    majors = MajorSerializers(many=True, read_only=True)
    user = UserBasicDecorators(read_only=True)


class PostElasticMappingDecorators(serializers.ModelSerializer):
    """
    elastic search mapping class
    """
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    thumb = serializers.CharField()
    intro = serializers.CharField(max_length=500)
    state = serializers.ChoiceField(choices=POST_STATE, default=-1)
    publish_time = serializers.CharField(required=False)
    categories = serializers.ListField(required=False, default=[])
    user = serializers.DictField(required=False, default=None)

    class Meta:
        model = Post
        fields = ('id', 'title', 'thumb', 'intro', 'state', 'publish_time', 'categories', 'user')

class PostListDecorators(PostElasticMappingDecorators):
    categories = CategorySerializers(many=True, read_only=True)
    user = UserBasicDecorators(read_only=True)

class PostListOutDecorators(serializers.Serializer):
    count = serializers.IntegerField(read_only=True)
    results = PostListDecorators(many=True, read_only=True)

class PostInDecorators(serializers.ModelSerializer):
    """
    decorator class
    """
    title = serializers.CharField(max_length=200)
    cover = serializers.ImageField()
    body = serializers.CharField()
    intro = serializers.CharField(max_length=500)
    state = serializers.ChoiceField(choices=POST_STATE, default=-1)
    publish_time = serializers.DateTimeField(required=False)
    
    class Meta:
        model = Post
        fields = ('title', 'cover', 'body', 'intro', 'state', 'publish_time', 'categories', 'majors')


class PostPartialInDecorators(PostInDecorators):
    """
    decorator class
    """
    title = serializers.CharField(max_length=200, required=False)
    cover = serializers.ImageField(required=False)
    body = serializers.CharField(required=False)
    intro = serializers.CharField(max_length=500, required=False)