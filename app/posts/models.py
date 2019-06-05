from datetime import datetime
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
from django.conf import settings
from django.db import models
from users.models import User
from job.models import Major

POST_STATE = [
    (-1, 'Draft'),
    (0, 'Not published'),
    (1, 'Published')
]

class Category(models.Model):
    """
    post's categories
    """

    display_name = models.CharField(max_length=50)

    def __str__(self):
        return self.display_name

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
    state = models.IntegerField(choices=POST_STATE, default=-1)
    publish_time = models.DateTimeField(default=datetime.now, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    majors = models.ManyToManyField(Major, blank=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def thumb_to_string(self):
        return self.thumb.url if self.thumb else None

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish_time', ]
