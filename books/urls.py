from django.urls import path
from .views import get_user

urlpatterns = [
    path("users/<str:username>/", get_user),
]