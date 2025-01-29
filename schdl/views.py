from django.http import JsonResponse
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from .models import BHP, LHP
from .serializers import BHPSerializer, LHPSerializer
import cloudinary.uploader
from cloudinary.uploader import upload
from datetime import timedelta
from django.utils.timezone import now

@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser])
def bhp_view(request):
    bhp_object, _ = BHP.objects.get_or_create(id=1)  # No need to handle DoesNotExist

    if request.method == 'GET':
        time_difference = now() - bhp_object.updated_at
        if time_difference > timedelta(hours=3):
            return JsonResponse({"message": "Image expired"}, status=status.HTTP_410_GONE)

        serializer = BHPSerializer(bhp_object)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

        # Delete old image if exists (keeping your original deletion method)
        if bhp_object.img:
            cloudinary.uploader.destroy(bhp_object.img.public_id, invalidate=True)
            cloudinary.uploader.destroy(bhp_object.pbid, invalidate=True)

        # Upload new image if provided (keeping direct access `request.FILES['img']`)
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


@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser])
def lhp_view(request):
    lhp_object, _ = LHP.objects.get_or_create(id=1)  # No need to handle DoesNotExist

    if request.method == 'GET':
        time_difference = now() - lhp_object.updated_at
        if time_difference > timedelta(hours=3):
            return JsonResponse({"message": "Image expired"}, status=status.HTTP_410_GONE)

        serializer = LHPSerializer(lhp_object)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

        # Delete old image if exists (keeping your original deletion method)
        if lhp_object.img:
            cloudinary.uploader.destroy(lhp_object.img.public_id, invalidate=True)
            cloudinary.uploader.destroy(lhp_object.pbid, invalidate=True)

        # Upload new image if provided (keeping direct access `request.FILES['img']`)
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
