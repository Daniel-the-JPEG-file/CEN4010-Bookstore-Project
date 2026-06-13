from django.http import JsonResponse
from .models import User


def get_user(request, username):
    try:
        user = User.objects.get(username=username)

        return JsonResponse({
            "username": user.username,
            "email": user.email,
            "home_address": user.home_address
        })

    except User.DoesNotExist:
        return JsonResponse(
            {"error": "User not found"},
            status=404
        )