from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializers import *
import json
import re
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from lxml import html 



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
                    # size = serializer.data['size'],
                    # url = serializer.data['url']
            )
            detail.save()
            
            return JsonResponse({'data': serializer.data})
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def scraper():
    data = ProductTag.objects.all().last()
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
    session = HTMLSession()
    page = session.get(data.url,headers=headers)
    

    return page.html.html

    

# from scrapping_app.views import scraper
# scraper()