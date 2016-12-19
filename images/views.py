from django.shortcuts import render
from django.http import HttpResponse
from wsgiref.util import FileWrapper

import PIL.Image
from cStringIO import StringIO

def index(request):
    return HttpResponse("Images index page.")

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from images.models import ServiceImage
from images.serializers import ServiceImageSerializer

class ServiceImageList(APIView):
    """
    List all images or create a new image.
    """
    queryset = ServiceImage.objects.all()

    def get(self, request, format=None):
        images = ServiceImage.objects.all()
        serializer = ServiceImageSerializer(images, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ServiceImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServiceImageDetail(APIView):
    """
    Retrieve or update an image instance.
    """
    queryset = ServiceImage.objects.all()

    def get_object(self, pk):
        try:
            return ServiceImage.objects.get(pk=pk)
        except ServiceImage.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        image = self.get_object(pk)
        serializer = ServiceImageSerializer(image)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        image = self.get_object(pk)
        serializer = ServiceImageSerializer(image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):
    #     image = self.get_object(pk)
    #     image.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

class ServiceImageData(APIView):
    """
    Retrieve or update an image file.
    """
    queryset = ServiceImage.objects.all()

    def get_object(self, pk):
        try:
            return ServiceImage.objects.get(pk=pk)
        except ServiceImage.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        image = self.get_object(pk)
        content_type = 'application/{}'.format(image.filetype)
        image_file = image.image
        if 'bbox' in request.query_params:
            # partial image requested
            # TODO: validate these
            x, y, w, h = request.query_params['bbox'].split(',')
            temporary_file = '{}:{}:{}:{}:{}'.format(x, y, w, h, image_file.name)
            print "Temporary file: {}".format(temporary_file)
            # major headaches with PIL file format -- couldn't just use file pointers
            # ended up saveing the cropped file and reopening it
            # open file in pillow
            img = PIL.Image.open(image.image.path)
            # crop file
            img2 = img.crop((0,0,10,10))
            # save temporary file
            img3 = img2.save('temp/' + temporary_file)
            # open for reading
            image_file = open('temp/' + temporary_file)
            # TODO: when can we delete the file?
        response = HttpResponse(FileWrapper(image_file), content_type=content_type)
        return response
