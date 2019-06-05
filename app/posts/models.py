from datetime import datetime
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
from django.conf import settings
from django.db import models
from category.models import Category

class Post(models.Model):
    """
    post
    """
    title = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='media', null=False, default='images.png')
    thumb = ImageSpecField(source='cover',
                            processors=[ResizeToFill(300, 200)],
                            format='JPEG',
                            options={'quality': 300})
    body = models.TextField()
    intro = models.CharField(max_length=500)
    categories = models.ManyToManyField(Category, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def thumb_to_string(self):
        return self.thumb.url if self.thumb else None

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created', ]
