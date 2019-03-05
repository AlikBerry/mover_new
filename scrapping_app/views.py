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
        lis1 =[]
        for x,y in request.data.items():
            clean = re.compile('>.*?<')
            text = re.sub(clean,'><',y)
            lis1.append(text)
            # val = list(request.data.keys())
            
                    
        # return JsonResponse({
        #     "status": "OK!",
        #     "name": lis1[0],
        #     "price": lis1[1],
        #     "size": lis1[2]
        
        # })
        serializer = DataInfo(data=request.data)
        if serializer.is_valid():
            detail = ProductTag(
                name = serializer.data['name'],
                price = serializer.data['price'],
                size = serializer.data['size'],
                url = serializer.data['url']
            )
            detail.save()
            return JsonResponse({'data':serializer.data})
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
