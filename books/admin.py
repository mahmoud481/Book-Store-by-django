from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from .forms import BookForm
from .models import Book, Category, Isbn, Tag


class BookAdmin(admin.ModelAdmin):
    form = BookForm
    list_display = ('title','author','content')
    list_filter = ('categories',)
    search_fields = ('title',)


class BookInline (admin.StackedInline):
    model = Book
    max_num = 3
    extra = 1

class TagAdmin(admin.ModelAdmin):
    inlines = [BookInline]

admin.site.register(Book,BookAdmin)
admin.site.register(Category)
admin.site.register(Isbn)
admin.site.register(Tag,TagAdmin)