from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import decorators, authenticate, login
from django.views import View

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework import permissions
from .models import Motel, ImageMotel
from rest_framework import viewsets
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView, )

from django.views.decorators.csrf import csrf_exempt
from .serializers import MotelSerializer, ImageSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

import json
from rest_framework import parsers
from django.http import QueryDict

from django.http import Http404
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView

class ImgUpload(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        posts_serializer = ImageSerializer(data= request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
# class PhongTroListCreateAPIView(viewsets.GenericViewSet,
#                                  ListCreateAPIView, ):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     # parser_classes = (FileUploadParser,)
#     parser_classes = (MultiPartParser, FormParser, FileUploadParser)
#     print("đây là hàm chính /.....")
#     serializer_class = MotelSerializer
#     queryset = baseInforMotel.objects.all()


#     def perform_create(self, serializer):
#         print(self.request)
#         serializer.save(owner=self.request.user)





class MotelPagination(PageNumberPagination): #Sắp xếp bài đăng 1 page 10 trang
    page_size = 10


class MotelList(generics.ListAPIView): #Liệt kê danh sách bài đăng phòng trọ api/motels/
    pagination_class = MotelPagination
    serializer_class = MotelSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Motel.objects.all()
        service_type = self.request.query_params.get('typeMotel')
        ward = self.request.query_params.get('ward')
        district = self.request.query_params.get('district')
        price = self.request.query_params.get('price')
        arc = self.request.query_params.get('arc')
        if service_type:
            queryset = queryset.filter(service_type=service_type)
        if ward:
            queryset = queryset.filter(ward__iexact=ward)
        if district:
            queryset = queryset.filter(district=district)
        if price:
            queryset = queryset.filter(price=price)
        if arc:
            queryset = queryset.filter(arc=arc)
        return queryset


class CreateMotelViews(generics.CreateAPIView): #Tạo bài đăng api/motels/create/
    queryset = Motel.objects.all()
    serializer_class = MotelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self): #Authentication user để tạo bài đăng
        query = Motel.objects.filter(user=self.request.user)
        return query

    def perform_create(self, serializer):
        print(self.request)
        serializer.save(user=self.request.user)


class MotelDetail(generics.RetrieveAPIView): #Get bài đăng api/motels/<id>
    permission_classes = (AllowAny,)
    queryset = Motel.objects.all()
    serializer_class = MotelSerializer


class MotelUpdate(generics.UpdateAPIView): #Cập nhật bài đăng api/motels/update/<pk>
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Motel.objects.all()
    serializer_class = MotelSerializer

    def get_queryset(self): #Authentication user để update
        query = Motel.objects.filter(user=self.request.user)
        return query


class MotelDelete(generics.DestroyAPIView): #Xóa bài bài đăng api/motels/delete/<pk>/
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = MotelSerializer

    def get_queryset(self): #Authentication user để xóa bài đăng
        query = Motel.objects.filter(user=self.request.user)
        return query


class PhotoUploadView(APIView): #Upload hình api/upload/
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        file_serializer = PhotoSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save(
                photo=request.data.get('pictures')
            )
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
