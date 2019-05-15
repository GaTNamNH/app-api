from django.db import models
from users.models import User
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill

class Post(models.Model):
    """
    post
    """
    name = models.CharField(max_length=75)
    file_upload = models.FileField(upload_to='media', null=False)
    image = models.ImageField(upload_to='media', null=False)
    image_thumb = ImageSpecField(source='image',
                                         processors=[ResizeToFill(80, 80)],
                                         format='JPEG',
                                         options={'quality': 80})


    # def get_image_thumb(self, obj):
    #     if obj.image:
    #         return obj.image_thumb.url or None
    #     return None

    def __str__(self):
        return self.name
