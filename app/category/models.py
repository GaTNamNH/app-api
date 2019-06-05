from django.db import models

# Create your models here.
class Category(models.Model):
    """
    post's categories
    """

    display_name = models.CharField(max_length=50)

    def __str__(self):
        return self.display_name