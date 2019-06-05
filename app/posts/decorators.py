from rest_framework import serializers
from .serializers import PostSerializers
from category.serializers import CategorySerializers
from .models import Post

class PostOutDecorators(PostSerializers):
    """
    decorator class
    """
    categories = CategorySerializers(many=True, read_only=True)

class PostInDecorators(serializers.ModelSerializer):
    """
    decorator class
    """
    title = serializers.CharField(max_length=200)
    cover = serializers.ImageField()
    body = serializers.CharField()
    intro = serializers.CharField(max_length=500)
    
    class Meta:
        model = Post
        fields = ('title', 'cover', 'body', 'intro', 'categories',)


class PostPartialInDecorators(PostInDecorators):
    """
    decorator class
    """
    title = serializers.CharField(max_length=200, required=False)
    cover = serializers.ImageField(required=False)
    body = serializers.CharField(required=False)
    intro = serializers.CharField(max_length=500, required=False)