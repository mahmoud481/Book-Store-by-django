import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from books.utils import create_new_ref_number

class Tag(models.Model):
    name = models.CharField(max_length=50)

class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    title = models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Isbn(models.Model):
    author_title = models.CharField(null=True,blank=True,max_length=50)
    book_title = models.CharField(null=True,blank=True,max_length=60)
    isbn_number = models.CharField(null=True,max_length=200, blank=True,unique=True,default=uuid.uuid4)


    def __str__(self):
        return f"{self.isbn_number}"

class Book(models.Model):
    title = models.CharField(max_length=255, default="")
    content = models.TextField(max_length=2048, default="")
    categories = models.ManyToManyField(Category)
    author = models.ForeignKey(User,null=True,on_delete=models.CASCADE,related_name='books')
    isbn = models.OneToOneField(Isbn,on_delete=models.CASCADE,null=True,blank=True)
    tag = models.ForeignKey(Tag,null=True,on_delete=models.CASCADE,related_name='books')
    def __str__(self):
        return self.title

