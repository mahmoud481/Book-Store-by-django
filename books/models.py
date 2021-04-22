from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
class Isbn(models.Model):
    author_title = models.CharField(null=True,blank=True,max_length=50)
    book_title = models.CharField(null=True,blank=True,max_length=60)
    isbn_number = models.IntegerField(null=True,auto_created=True)

class Book(models.Model):
    title = models.CharField(max_length=255, default="")
    content = models.TextField(max_length=2048, default="")
    categories = models.ManyToManyField(Category)
    author = models.ForeignKey(User,null=True,on_delete=models.CASCADE,related_name='books')
    isbn = models.OneToOneField(Isbn,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.title

