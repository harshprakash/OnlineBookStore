from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model
from PIL import Image

#  database creation for Book
class Book(models.Model):
    title = models.CharField(max_length=180)
    authors = models.CharField(max_length=180)
    cover = models.ImageField(default="none",upload_to='profile_pics')
    price = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title
    # database Name
    class Meta:
        db_table = "Book"
     