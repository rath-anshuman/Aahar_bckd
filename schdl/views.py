from django.http import JsonResponse
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from .models import BHP, LHP
from .serializers import BHPSerializer, LHPSerializer
import cloudinary
from cloudinary.uploader import upload
from django.utils.timezone import now
from datetime import timedelta, date
from account.models import Visitor




@api_view(['GET'])
@permission_classes([AllowAny])
def bhp_get_view(request):
    try:
        bhp_object = BHP.objects.get(id=1)
        time_difference = now() - bhp_object.updated_at
        if time_difference > timedelta(hours=3):
            return JsonResponse({"message": "Image expired"}, status=status.HTTP_410_GONE)

        serializer = BHPSerializer(bhp_object)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    except BHP.DoesNotExist:
        return JsonResponse({'error': 'BHP object with id=1 does not exist'}, status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def bhp_post_view(request):
    try:
        bhp_object, created = BHP.objects.get_or_create(id=1)

        if bhp_object.img:
            cloudinary.uploader.destroy(bhp_object.img.public_id, invalidate=True)
            cloudinary.uploader.destroy(bhp_object.pbid, invalidate=True)

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


@api_view(['GET'])
@permission_classes([AllowAny])
def lhp_get_view(request):
    try:
        lhp_object = LHP.objects.get(id=1)
        time_difference = now() - lhp_object.updated_at
        if time_difference > timedelta(hours=3):
            return JsonResponse({"message": "Image expired"}, status=status.HTTP_410_GONE)

        serializer = LHPSerializer(lhp_object)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    except LHP.DoesNotExist:
        return JsonResponse({'error': 'LHP object with id=1 does not exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def lhp_post_view(request):
    try:
        lhp_object, created = LHP.objects.get_or_create(id=1)

        if lhp_object.img:
            cloudinary.uploader.destroy(lhp_object.img.public_id, invalidate=True)
            cloudinary.uploader.destroy(lhp_object.pbid, invalidate=True)

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
