from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializers import *
import json

# Create your views here.
class ApiIndexView(APIView):

    def get(self,requests,*args, **kwargs):
        return JsonResponse({'data':"OK"})

    def post(self,requests,*args, **kwargs):
        serializer = DataInfo(data=requests.data)
        if serializer.is_valid():
            price = Data(
                price = serializer.data['price']
            )
            price.save()
            return JsonResponse({'data':serializer.data})
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)