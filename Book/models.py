from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model
from PIL import Image

#  database creation for Book
class Book(models.Model):   
    title = models.CharField(max_length=180)   # Title of the book
    authors = models.CharField(max_length=180) # Author of the book 
    cover = models.ImageField(default="none",upload_to='profile_pics') # image of book cover
    price = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title
    # database Name
    class Meta:
        db_table = "Book"
     
