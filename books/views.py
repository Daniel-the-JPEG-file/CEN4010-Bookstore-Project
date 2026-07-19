from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def books_by_genre(request, genre):
    books = Book.objects.filter(genre__iexact=genre)
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
from django.shortcuts import render

@api_view(['GET'])
def top_sellers(request):
    # The '-' in front of 'copies_sold' sorts the list from highest to lowest
    books = Book.objects.order_by('-copies_sold')[:10]
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def books_by_price(request, order):
    # Sort low to high
    if order == 'asc':
        books = Book.objects.order_by('price')
    # Sort high to low
    elif order == 'desc':
        books = Book.objects.order_by('-price')
    # Fallback if they type something wrong
    else:
        books = Book.objects.all()

    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)