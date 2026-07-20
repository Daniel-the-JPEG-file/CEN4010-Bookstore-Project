from rest_framework import serializers
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