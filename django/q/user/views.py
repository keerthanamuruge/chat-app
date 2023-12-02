from django.shortcuts import render
from .models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view()
def get_user(request):
    users = User.objects.all()
    user_data = [{'id': user.id, 'username': user.username} for user in users]
    print(user_data)
    return Response(user_data)
