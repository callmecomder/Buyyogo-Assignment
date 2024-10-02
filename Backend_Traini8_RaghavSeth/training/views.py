# training/views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TrainingCenter
from .serializers import TrainingCenterSerializer

@api_view(['POST'])
def create_training_center(request):
    serializer = TrainingCenterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_training_centers(request):
    centers = TrainingCenter.objects.all()
    serializer = TrainingCenterSerializer(centers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

