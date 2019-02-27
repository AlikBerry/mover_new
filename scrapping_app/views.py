from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializers import *
import json
# Create your views here.

#def scrapping(request):
#    context = {}
#    context['Products'] = SelectedProducts.objects.all()  
#    
#    return render(request,"index.html",context)


class ApiIndexView(APIView):

    def get(self,request,*args, **kwargs):
        return JsonResponse({'data':"OK"})

    def post(self,request,*args, **kwargs):
        return JsonResponse({
            "data": request.data,
            "ishledi":"broo"
        })
        # serializer = DataInfo(data=requests.data)
        # if serializer.is_valid():
        #     price = Data(
        #         price = serializer.data['price']
        #     )
        #     price.save()
        #     return JsonResponse({'data':serializer.data})
        # return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
