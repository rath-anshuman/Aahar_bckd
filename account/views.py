from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    pssd = request.data.get('password')

    user = authenticate(username=username, password=pssd)

    if user is None:
        return Response({'error': 'Invalid credentials'}, status=400)
    else:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'username': user.username})

@csrf_exempt
@api_view(['POST'])
def logout(request):
    try:
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response({'message': 'Successfully logged out'}, status=200)
    except Token.DoesNotExist:
        return Response({'error': 'Invalid request or user not logged in'}, status=400)