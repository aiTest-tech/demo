from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class DemoView(APIView):
  def get(self, request, *args, **kwargs):
    return Response({"name":"demo", "email":"demo@gmail.com", "phone":1234}, status=status.HTTP_200_OK)