from django.urls import path
from .views import get_user, get_credit_cards, create_user

urlpatterns = [

    path(
        "users/create/",
        create_user
    ),

    path(
        "users/<str:username>/",
        get_user
    ),

    path(
        "users/<str:username>/creditcards/",
        get_credit_cards
    ),

]