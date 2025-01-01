from django.http import JsonResponse
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view, parser_classes
from rest_framework import status
from cloudinary.uploader import destroy
from .models import BHP, LHP
from .serializers import BHPSerializer, LHPSerializer


@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser])
def bhp_view(request):
    """
    Handle both GET and POST requests for the single BHP object (id=1).
    """
    return handle_image_view(request, BHP, BHPSerializer, "BHP")


@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser])
def lhp_view(request):
    """
    Handle both GET and POST requests for the single LHP object (id=1).
    """
    return handle_image_view(request, LHP, LHPSerializer, "LHP")


def handle_image_view(request, model, serializer_class, model_name):
    """
    Handle GET and POST requests for models with a single image object.
    Automatically replaces images when a new one is uploaded.

    Args:
        request: The HTTP request.
        model: The model class (e.g., BHP or LHP).
        serializer_class: The serializer class (e.g., BHPSerializer or LHPSerializer).
        model_name: Name of the model (used for error messages).

    Returns:
        JsonResponse: The response to the client.
    """
    try:
        # Get or create the object with id=1
        obj, created = model.objects.get_or_create(id=1)

        if request.method == 'GET':
            # Serialize and return the object data
            serializer = serializer_class(obj)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

        elif request.method == 'POST':
            # If a new image is provided, delete the old one
            if 'img' in request.data and obj.public_id:
                destroy(obj.public_id)  # Delete the existing image from Cloudinary

            # Update the object with new data
            serializer = serializer_class(obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=status.HTTP_200_OK)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except model.DoesNotExist:
        return JsonResponse(
            {'error': f'{model_name} object with id=1 does not exist'},
            status=status.HTTP_404_NOT_FOUND
        )
