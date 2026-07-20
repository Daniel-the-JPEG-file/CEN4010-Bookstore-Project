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
from .models import User, CreditCard

# handles converting User model data to and from JSON
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }


# handles converting CreditCard model data to and from JSON
class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = '__all__'