import json
from django.views.decorators.csrf import csrf_exempt
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
def get_credit_cards(request, username):

    try:

        user = User.objects.get(username=username)

        cards = user.credit_cards.all()

        data = []

        for card in cards:

            data.append({
                "cardholder_name": card.cardholder_name,
                "card_last_four": card.card_number[-4:],
                "expiration_date": card.expiration_date
            })

        return JsonResponse(data, safe=False)

    except User.DoesNotExist:

        return JsonResponse(
            {"error": "User not found"},
            status=404
        )

@csrf_exempt
def create_user(request):

    if request.method != "POST":
        return JsonResponse(
            {"error": "Only POST requests are allowed"},
            status=405
        )

    try:
        data = json.loads(request.body)

        required_fields = [
            "username",
            "password",
            "email",
            "home_address"
        ]

        for field in required_fields:
            if field not in data:
                return JsonResponse(
                    {"error": f"Missing field: {field}"},
                    status=400
                )

        if User.objects.filter(username=data["username"]).exists():
            return JsonResponse(
                {"error": "Username already exists"},
                status=400
            )

        user = User.objects.create(
            username=data["username"],
            password=data["password"],
            first_name=data.get("first_name", ""),
            last_name=data.get("last_name", ""),
            email=data["email"],
            home_address=data["home_address"]
        )

        return JsonResponse(
            {
                "message": "User created successfully",
                "username": user.username
            },
            status=201
        )

    except json.JSONDecodeError:
        return JsonResponse(
            {"error": "Invalid JSON"},
            status=400
        )

    except Exception as e:
        return JsonResponse(
            {"error": str(e)},
            status=500
        )