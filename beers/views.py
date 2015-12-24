from django.shortcuts import render

# Create your views here.
from beers.models import Beer
from beers.serializer import BeerSerializer
from rest_framework import generics
 
 
# List our beers and add beers
class BeerList(generics.ListCreateAPIView):
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer
 
 
# Get a beer and remove a beer
class BeerDetail(generics.RetrieveDestroyAPIView):
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer