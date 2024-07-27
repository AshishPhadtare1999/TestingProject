from django.shortcuts import render,HttpResponse
from .models import *
from django.contrib.auth.models import Group, User
from rest_framework import viewsets
# Create your views here.
from customer.serializer import GroupSerializer,UserSerializer

def CustomerView(request):
    data=Customer.objects.all()
    return HttpResponse("This is data....")

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all() 
    serializer_class=UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset=Group.objects.all()
    serializer_class=GroupSerializer