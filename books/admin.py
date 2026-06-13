from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import User, CreditCard
# or whatever your model names are

admin.site.register(User)
admin.site.register(CreditCard)