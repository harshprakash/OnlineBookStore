from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Book(models.Model):
    title = models.CharField(max_length=180)
    authors = models.CharField(max_length=180)
    cover = models.ImageField()
    price = models.PositiveIntegerField()
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = "Book"
     