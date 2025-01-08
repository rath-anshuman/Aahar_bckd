from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status

# @api_view(['POST'])
def token_obtain(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return JsonResponse({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }, status=200)
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
    return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


# @api_view(['POST'])
def token_refresh(request):
    if request.method == 'POST':
        refresh_token = request.POST.get('refresh')

        if not refresh_token:
            return JsonResponse({'error': 'Refresh token is required'}, status=400)

        try:
            refresh = RefreshToken(refresh_token)
            return JsonResponse({
                'access': str(refresh.access_token),
            }, status=200)
        except Exception as e:
            return JsonResponse({'error': 'Invalid refresh token'}, status=401)

    return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)