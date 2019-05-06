from django.db import models

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
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag)