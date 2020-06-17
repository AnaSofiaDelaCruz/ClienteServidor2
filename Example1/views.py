from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from django.http import Http404
from django.shortcuts import get_object_or_404

#Importacion Modelos 

from Example1.models import Example1

#Importaciones Serializers 
from Example1.serializer import Example1Serializers


class ExampleList(APIView):
    def get(self, request, format=None):
        print("GET")
        queryset = Example1.objects.all()
        serializer = Example1Serializers(queryset, many = True)
        return Response(serializer.data)