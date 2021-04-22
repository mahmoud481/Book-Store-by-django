from django.contrib import admin

# Register your models here.
from .models import Book,Category,Isbn

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Isbn)