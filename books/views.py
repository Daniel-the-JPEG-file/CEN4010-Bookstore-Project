from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Book, Author, User, CreditCard
from .serializers import BookSerializer, AuthorSerializer, UserSerializer, CreditCardSerializer
# views handle the logic for each API endpoint
# each function here corresponds to a specific URL and HTTP request type

# create a book
# 201 created if functional
@api_view(['POST']) # only accepts POST requests (sending data)
def create_book(request): # contains the JSON data sent by the client
    serializer = BookSerializer(data = request.data) # serializes data from JSON
    if serializer.is_valid():
        serializer.save()
        return Response(status = status.HTTP_201_CREATED) # success
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) # failure

# Get a book by ISBN
@api_view(['GET']) # only accepts GET requests (retrieving data)
def get_book(request, isbn):
    try: # tries finding book in database with matching ISBN
        book = Book.objects.get(ISBN = isbn) # returns book with corresponding ISBN
    except Book.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND) # failure
    serializer = BookSerializer(book) # converts book to JSON and returns JSON data
    return Response(serializer.data)

# Create an author
# functions same as create_book
@api_view(['POST']) # only accepts POST requests (sending data)
def create_author(request):
    serializer = AuthorSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Get all books by an author
# returns a list
@api_view(['GET']) # only accepts GET requests (retrieving data)
def get_books_by_author(request, author_id): # searches database for author ID
    books = Book.objects.filter(author = author_id) # returns list of books from the author ID
    serializer = BookSerializer(books, many = True) # convert to JSON ; many = True means expect a list
    return Response(serializer.data)


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
