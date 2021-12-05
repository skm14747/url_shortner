from django.http import response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import redirect

from .serializers import UrlSerializer
from .models import HitsLog, Url


class UrlView(APIView):
 
    def post(self, request):
        try:
            url = Url(url=request.data["url"])
            url.save()
            urls = UrlSerializer(url)
            return Response(urls.data, status=status.HTTP_201_CREATED)
        except ValueError as v:
            return Response({"message":str(v)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message":"Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, short_code):
        try:
            url = Url.objects.get(short_code = short_code)
            urls = UrlSerializer(url)
            return Response(urls.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":"Invalid short Url"}, status=status.HTTP_400_BAD_REQUEST)
        
    
    
class RootView(APIView):
    
    def get(self, request, short_code):
        try:
            url = Url.objects.get(short_code = short_code)
            
            hits_log = HitsLog(url_id=url.id)
            hits_log.save()
            
            response = redirect(url.url)
            return response
        except Exception as e:
            return Response("bad request", status=status.HTTP_400_BAD_REQUEST)