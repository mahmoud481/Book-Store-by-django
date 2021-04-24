from rest_framework import serializers
# from rest_framework.serializers import ModelSerializer

from books.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model= Book
        fields = ("title","content", "author")