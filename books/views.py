from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
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