from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from .models import Visitor
from datetime import date

VISITOR_DOMAIN = "https://new-aahar.vercel.app"
LOGIN_DOMAIN="https://menu-admin-gules.vercel.app/adminpage.html"

@csrf_exempt
@api_view(['POST'])
def login(request):

    origin = request.META.get('HTTP_ORIGIN', '')
    referer = request.META.get('HTTP_REFERER', '')

    if LOGIN_DOMAIN not in origin and LOGIN_DOMAIN not in referer:
        return JsonResponse({"error": "Unauthorized domain"}, status=403)
    
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
        return JsonResponse({'message': 'Successfully logged out'}, status=200)
    except Token.DoesNotExist:
        return JsonResponse({'error': 'Invalid request or user not logged in'}, status=400)



@csrf_exempt
@api_view(['POST'])
def visitorplus(request):
    origin = request.META.get('HTTP_ORIGIN', '')
    referer = request.META.get('HTTP_REFERER', '')

    if VISITOR_DOMAIN not in origin and VISITOR_DOMAIN not in referer:
        return JsonResponse({"error": "Unauthorized domain"}, status=403)
    if request.method == 'POST':
        today = date.today()
        visitor, created = Visitor.objects.get_or_create(day=today)
        visitor.count += 1
        visitor.save()
        return JsonResponse({f'{today}':visitor.count})