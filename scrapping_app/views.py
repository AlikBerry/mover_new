from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializers import *
import json
import re



class ApiIndexView(APIView):

    def get(self,request,*args, **kwargs):
        return JsonResponse({'status':"OK"})

    def post(self, request, *args, **kwargs):
        
        clean_data = {}

        for k, v in request.data.items():
                clean = re.compile('>.*?<')
                texts = re.sub(clean,'><',v)
                clean_data.update({k:texts})
            
        serializer = DataInfo(data=clean_data)
        if serializer.is_valid():
            if serializer.is_valid():
                detail = ProductTag(
                    # name = serializer.data['name'],
                    price = serializer.data['price'],
                    size = serializer.data['size'],
                    # url = serializer.data['url']
            )
            detail.save()
            
            return JsonResponse({'data': serializer.data})
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
