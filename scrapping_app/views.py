from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializers import *
import json
import re
# Create your views here.

#def scrapping(request):
#    context = {}
#    context['Products'] = SelectedProducts.objects.all()  
#    
#    return render(request,"index.html",context)


class ApiIndexView(APIView):

    def get(self,request,*args, **kwargs):
        return JsonResponse({'status':"OK"})

    def post(self, request, *args, **kwargs):
        for x,y in request.data.items():
            print(x, y)
            clean = re.compile('>.*?<')
            text = re.sub(clean,'><',y)
            print(text)
            
        return JsonResponse({
            "status": "OK!",
            "ad": text,
            "qiymet": text,
            "razmer": text
        })
        # serializer = DataInfo(data=requests.data)
        # if serializer.is_valid():
        #     price = Data(
        #         price = serializer.data['price']
        #     )
        #     price.save()
        #     return JsonResponse({'data':serializer.data})
        # return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
