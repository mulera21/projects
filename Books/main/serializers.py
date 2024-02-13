from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ['id', 'title', 'author']
