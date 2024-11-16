from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'birthdate']

class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.name')  # For displaying author name

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'author_name', 'published_date', 'isbn', 'available']
