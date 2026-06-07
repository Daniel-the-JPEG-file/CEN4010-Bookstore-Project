from rest_framework import serializers
from .models import Book, Author
# serializers convert database models to JSON format and vice versa

# handles converting Author model data to and from JSON
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

# handles converting Book model data to and from JSON
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'