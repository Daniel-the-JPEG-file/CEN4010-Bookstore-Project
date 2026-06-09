from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg
from .models import Book, Rating, Comment


# GET /api/books/<book_id>/comments/
@api_view(['GET'])
def get_comments(request, book_id):
    comments = Comment.objects.filter(book_id=book_id)
    data = [
        {
            'id': c.id,
            'user': c.user,
            'text': c.text,
            'created_at': c.created_at,
        }
        for c in comments
    ]
    return Response(data)


# GET /api/books/<book_id>/rating/
@api_view(['GET'])
def get_average_rating(request, book_id):
    avg = Rating.objects.filter(book_id=book_id).aggregate(Avg('score'))['score__avg']
    if avg is None:
        return Response({'average_rating': None, 'message': 'No ratings yet'})
    return Response({'average_rating': round(avg, 2)})


# POST /api/books/<book_id>/comments/
@api_view(['POST'])
def create_comment(request, book_id):
    user = request.data.get('user')
    text = request.data.get('text')
    if not user or not text:
        return Response({'error': 'user and text are required'}, status=status.HTTP_400_BAD_REQUEST)
    comment = Comment.objects.create(book_id=book_id, user=user, text=text)
    return Response({'id': comment.id, 'user': comment.user, 'text': comment.text}, status=status.HTTP_201_CREATED)


# POST /api/books/<book_id>/rating/
@api_view(['POST'])
def create_rating(request, book_id):
    user = request.data.get('user')
    score = request.data.get('score')
    if not user or score is None:
        return Response({'error': 'user and score are required'}, status=status.HTTP_400_BAD_REQUEST)
    if not (1 <= int(score) <= 5):
        return Response({'error': 'score must be between 1 and 5'}, status=status.HTTP_400_BAD_REQUEST)
    rating = Rating.objects.create(book_id=book_id, user=user, score=score)
    return Response({'id': rating.id, 'user': rating.user, 'score': rating.score}, status=status.HTTP_201_CREATED)