from django.urls import path
from .views import (
    create_user,
    get_user,
    update_user,
    create_credit_card,
    get_credit_cards,
)

urlpatterns = [
    path("users/create/", create_user),

    path("users/<str:username>/", get_user),

    path("users/<str:username>/update/", update_user),

    path("users/<str:username>/creditcards/", create_credit_card),

    path("users/<str:username>/creditcards/list/", get_credit_cards),
]