from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User, CreditCard
from .serializers import UserSerializer, CreditCardSerializer


# Defines a GET USER endpoint.

@api_view(['GET'])
def get_user(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user)
    return Response(serializer.data)

#UPDATE USER PUT ENDPOINT

@api_view(['PUT', 'PATCH'])
def update_user(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Email should not be updated according to the project requirements.
    data = request.data.copy()
    data.pop("email", None)

    serializer = UserSerializer(user, data=data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Defines a POST user endpoint

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Defines a GET CREDIT CARD ENDPOINT

@api_view(['GET'])
def get_credit_cards(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    cards = CreditCard.objects.filter(user=user)

    serializer = CreditCardSerializer(cards, many=True)

    return Response(serializer.data)

#Create Credit Card POST ENDPOINT

@api_view(['POST'])
def create_credit_card(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CreditCardSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(user=user)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)