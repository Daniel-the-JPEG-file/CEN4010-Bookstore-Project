from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book, CartItem
from .serializers import BookSerializer, CartItemSerializer

# GET - Retrieve list of books in user's cart
@api_view(['GET'])
def get_cart(request, user_id):
    items = CartItem.objects.filter(user_id=user_id)
    serializer = CartItemSerializer(items, many=True)
    return Response(serializer.data)

# GET - Retrieve subtotal of all items in user's cart
@api_view(['GET'])
def get_subtotal(request, user_id):
    items = CartItem.objects.filter(user_id=user_id)
    subtotal = sum(item.book.price for item in items)
    return Response({'subtotal': subtotal})

# POST - Add a book to the cart
@api_view(['POST'])
def add_to_cart(request):
    user_id = request.data.get('user_id')
    book_id = request.data.get('book_id')
    try:
        book = Book.objects.get(id=book_id)
        CartItem.objects.create(user_id=user_id, book=book)
        return Response({'message': 'Book added to cart'}, status=status.HTTP_201_CREATED)
    except Book.DoesNotExist:
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

# DELETE - Remove a book from the cart
@api_view(['DELETE'])
def remove_from_cart(request):
    user_id = request.data.get('user_id')
    book_id = request.data.get('book_id')
    try:
        item = CartItem.objects.get(user_id=user_id, book_id=book_id)
        item.delete()
        return Response({'message': 'Book removed from cart'}, status=status.HTTP_200_OK)
    except CartItem.DoesNotExist:
        return Response({'error': 'Item not found in cart'}, status=status.HTTP_404_NOT_FOUND)