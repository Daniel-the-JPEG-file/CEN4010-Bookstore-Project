from django.urls import path
from . import views

urlpatterns = [
    path('books/<int:book_id>/comments/', views.get_comments, name='get_comments'),
    path('books/<int:book_id>/rating/', views.get_average_rating, name='get_average_rating'),
    path('books/<int:book_id>/comments/create/', views.create_comment, name='create_comment'),
    path('books/<int:book_id>/rating/create/', views.create_rating, name='create_rating'),
]