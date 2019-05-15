from rest_framework import serializers
from .models import Post

class PostSerializers(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=75)
    file_upload = serializers.FileField()
    image = serializers.ImageField()
    image_thumb = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'name', 'file_upload', 'image', 'image_thumb', )

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
    
    def get_image_thumb(self, obj):
        if obj.image:
            return obj.image_thumb.url or None
        return None


class PostInputSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=75)
    file_upload = serializers.FileField()
    image = serializers.ImageField()

    class Meta:
        model = Post


