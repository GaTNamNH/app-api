from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

# Create your models here.
class Category(models.Model):
    """
    todo's category
    """

    title = models.CharField(max_length=200)

class Tag(models.Model):
    """
    todo's tags
    """

    title = models.CharField(max_length=200)

class Todo(models.Model):
    """
    todo
    """

    subject = models.CharField(max_length=200)
    content = models.CharField(max_length=400)
    timer = models.TimeField()
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag)