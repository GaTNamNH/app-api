from django.db import models

# Create your models here.
class Todo(models.Model):
    """
    todo
    """

    subject = models.CharField(max_length=200)
    content = models.CharField(max_length=400)
    timer = models.TimeField()
    created = models.DateTimeField(auto_now_add=True)
