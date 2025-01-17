from django.http import JsonResponse
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from .models import BHP, LHP
from .serializers import BHPSerializer, LHPSerializer
import cloudinary
from cloudinary.uploader import upload


@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser])
def bhp_view(request):
    """
    Handle both GET and POST requests for the single BHP object (id=1).
    """
    try:
        bhp_object, created = BHP.objects.get_or_create(id=1)

        # Handle GET request
        if request.method == 'GET':
            # Allow any user for GET request
            permission_classes = [AllowAny]
            serializer = BHPSerializer(bhp_object)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

        # Handle POST request
        elif request.method == 'POST':
            # Enforce authentication for POST request
            permission_classes = [IsAuthenticated]
            if not request.user.is_authenticated:
                return JsonResponse({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

            # Delete old image from Cloudinary if it exists
            if bhp_object.img:
                cloudinary.uploader.destroy(bhp_object.img.public_id)

            # Handle new image upload from request
            if 'img' in request.FILES:
                # Upload new image to Cloudinary
                new_img = request.FILES['img']
                print(new_img)
                cloudinary_response = upload(new_img)
                # Save the new image URL or public_id to the model
                bhp_object.img = cloudinary_response['secure_url']  # or cloudinary_response['public_id'] if using public_id
                bhp_object.save()

            # Update other fields if needed
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

        # Handle GET request
        if request.method == 'GET':
            # Allow any user for GET request
            permission_classes = [AllowAny]
            serializer = LHPSerializer(lhp_object)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

        # Handle POST request
        elif request.method == 'POST':
            # Enforce authentication for POST request
            permission_classes = [IsAuthenticated]
            if not request.user.is_authenticated:
                return JsonResponse({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

            # Delete old image from Cloudinary if it exists
            if lhp_object.img:
                cloudinary.uploader.destroy(lhp_object.img.public_id)

            # Handle new image upload from request
            if 'img' in request.FILES:
                # Upload new image to Cloudinary
                new_img = request.FILES['img']
                cloudinary_response = upload(new_img)
                # Save the new image URL or public_id to the model
                lhp_object.img = cloudinary_response['secure_url']  # or cloudinary_response['public_id']
                lhp_object.save()

            # Update other fields if needed
            serializer = LHPSerializer(lhp_object, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=status.HTTP_200_OK)

            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except LHP.DoesNotExist:
        return JsonResponse({'error': 'LHP object with id=1 does not exist'}, status=status.HTTP_404_NOT_FOUND)