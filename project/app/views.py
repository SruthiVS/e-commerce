from django.shortcuts import render
from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *


class CustomerReg(generics.ListCreateAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer

class CustomerDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Customer
    serializer_class=CustomerSerializer


# PRODUCT

class ProductList(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product
    serializer_class=ProductSerializer

class ProdView(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer