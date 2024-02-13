from rest_framework import viewsets
from .models import Book
from .import serializers

# Create your views here.
class Bookviewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializers_class = serializers.BookSerializer
