from django.http import JsonResponse
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from .models import BHP, LHP
from .serializers import BHPSerializer, LHPSerializer
import cloudinary
from cloudinary.uploader import upload



from datetime import date
from account.models import Visitor

def add_visitor():
    today = date.today()
    visitor, created = Visitor.objects.get_or_create(day=today)
    visitor.count += 1
    visitor.save()




@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser])
def bhp_view(request):
    """
    Handle both GET and POST requests for the single BHP object (id=1).
    """
    try:
        bhp_object, created = BHP.objects.get_or_create(id=1)
        if request.method == 'GET':
            permission_classes = [AllowAny]
            serializer = BHPSerializer(bhp_object)
            add_visitor()
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

        elif request.method == 'POST':
            permission_classes = [IsAuthenticated]
            if not request.user.is_authenticated:
                return JsonResponse({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

            if bhp_object.img:
                cloudinary.uploader.destroy(bhp_object.img.public_id,invalidate=True)
                cloudinary.uploader.destroy(bhp_object.pbid,invalidate=True)

            if 'img' in request.FILES:
                new_img = request.FILES['img']
                cloudinary_response = upload(new_img)
                bhp_object.img = cloudinary_response['secure_url']  
                bhp_object.pbid = cloudinary_response['public_id']  
                bhp_object.save()

            serializer = BHPSerializer(bhp_object, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=status.HTTP_200_OK)

            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except BHP.DoesNotExist:
        return JsonResponse({'error': 'BHP object with id=1 does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser])
def lhp_view(request):
    """
    Handle both GET and POST requests for the single LHP object (id=1).
    """
    try:
        lhp_object, created = LHP.objects.get_or_create(id=1)
        if request.method == 'GET':
            permission_classes = [AllowAny]
            serializer = LHPSerializer(lhp_object)
            add_visitor()
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

        elif request.method == 'POST':
            permission_classes = [IsAuthenticated]
            if not request.user.is_authenticated:
                return JsonResponse({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

            if lhp_object.img:
                cloudinary.uploader.destroy(lhp_object.img.public_id,invalidate=True)
                cloudinary.uploader.destroy(lhp_object.pbid,invalidate=True)

            if 'img' in request.FILES:
                new_img = request.FILES['img']
                cloudinary_response = upload(new_img)
                lhp_object.img = cloudinary_response['secure_url']
                lhp_object.pbid = cloudinary_response['public_id'] 
                lhp_object.save()

            serializer = LHPSerializer(lhp_object, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=status.HTTP_200_OK)

            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except LHP.DoesNotExist:
        return JsonResponse({'error': 'LHP object with id=1 does not exist'}, status=status.HTTP_404_NOT_FOUND)