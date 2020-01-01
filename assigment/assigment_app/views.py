from django.shortcuts import render
from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .models import Product
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializers
from rest_framework import status

# Create your views here.

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def Product_list(request,format=None):
    if request.method == 'GET':
        obj = Product.objects.all()
        serializer = ProductSerializers(obj,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




#for view using id 
@api_view(['GET','PUT'])
def Product_details(request,idk ,format=None):
    try:
        obj = Product.objects.get(id=idk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductSerializers(obj)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializers(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(seralizer.errors,status=status.HTTP_404_BAD_REQUEST) 
