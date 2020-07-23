from django.shortcuts import render
from rest_framework import viewsets
from .models import Photo
from .serializers import PhotoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


from django.conf import settings
import os

import cv2
from .classifiyfile import Classify_image


class PhotoImageView(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    
    
@api_view(['GET'])
def allImages(request):
    images_queryset = Photo.objects.all()
    serializer = PhotoSerializer(images_queryset,many = True)
    return Response(serializer.data)
    
@api_view(['GET'])
def imageResult(request,pk):
    image = Photo.objects.get(id=pk)
    path = os.path.join(settings.MEDIA_ROOT, os.path.normpath(str(image.image)))
    print("path ===>",path)
    serializer = PhotoSerializer(image,many = False)
    resulting_image,personlist = Classify_image(path)
    ans = {
        'person':personlist
    }
    return Response(ans)