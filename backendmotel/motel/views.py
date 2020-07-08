from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render
from django.contrib.auth import decorators, authenticate, login
from django.views import View

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework import permissions
from .models import Motel, ImageMotel
from user.models import User
from rest_framework import viewsets
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView, )

from django.views.decorators.csrf import csrf_exempt
from .serializers import MotelSerializer, ImageSerializer, GetMotelSerializer
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

# class MotelListLatest(generics.ListAPIView):
#     permission_classes = (AllowAny,)
#     pagination_class = MotelPagination
#     serializer_class = GetMotelSerializer

#     # def get_queryset(self):
#     #     queryset = Motel.objects.filter().order_by('-created_at')
#     #     return queryset 

#     def get(self, request):
#         queryset = Motel.objects.filter().order_by('-created_at')
#         serializer = GetMotelSerializer(queryset)
#         return Response(serializer.data)


class MotelListLatest(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        queryset = Motel.objects.filter().order_by('-created_at')
        serializer = GetMotelSerializer(queryset, many=True)
        return Response(serializer.data)


class MotelList(generics.ListAPIView): #Liệt kê danh sách bài đăng phòng trọ api/motels/
    pagination_class = MotelPagination
    serializer_class = GetMotelSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Motel.objects.all()
        idprice = self.request.query_params.get('price')
        if idprice == '0':
            idprice = '8'
        id_price = int(idprice)

        idarc = self.request.query_params.get('arc')
        if idarc == '0':
            idarc = '8'
        id_arc = int(idarc)
        service_type = self.request.query_params.get('typeMotel')
        ward = self.request.query_params.get('ward')
        district = self.request.query_params.get('district')

        if service_type and service_type != '0':
            queryset = queryset.filter(typeMotel=service_type)
            print("đây là query cho type")
        if ward and ward != '0':
            queryset = queryset.filter(ward__iexact=ward)
            print("đây là query cho ward")
        if district and district!='0':
            queryset = queryset.filter(district=district)
            print("đây là query cho district ")

        if id_price == 0:
            queryset = queryset.filter(price__lt=1000000)
        if id_price == 1:
            queryset = queryset.filter(price__gt=1000000, price__lt=2000000)
        if id_price == 2:
            queryset = queryset.filter(price__gt=2000000, price__lt=3000000)
        if id_price == 3:
            queryset = queryset.filter(price__gt=3000000, price__lt=5000000)
        if id_price == 4:
            queryset = queryset.filter(price__gt=5000000, price__lt=7000000)
        if id_price == 5:
            queryset = queryset.filter(price__gt=7000000, price__lt=10000000)
        if id_price == 6:
            queryset = queryset.filter(price__gt=10000000, price__lt=15000000)
        if id_price == 7:
            queryset = queryset.filter(price__gt=15000000)
        if id_arc == 0:
            queryset = queryset.filter(arc__lt=20)
        if id_arc == 1:
            queryset = queryset.filter(arc__gt=20, arc__lt=30)
        if id_arc == 2:
            queryset = queryset.filter(arc__gt=30, arc__lt=50)
        if id_arc == 3:
            queryset = queryset.filter(arc__gt=50, arc__lt=60)
        if id_arc == 4:
            queryset = queryset.filter(arc__gt=60, arc__lt=70)
        if id_arc == 5:
            queryset = queryset.filter(arc__gt=70, arc__lt=80)
        if id_arc == 6:
            queryset = queryset.filter(arc__gt=80, arc__lt=90)
        if id_arc == 7:
            queryset = queryset.filter(arc__gt=100)
        return queryset



# class GetMyPost(generics.ListAPIView): # Lấy bài đăng của user
#     queryset = Motel.objects.all()
#     serializer_class = MotelSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self): 
#         print(self.request.user.id)
#         queryset = super(GetMyPost, self).get_queryset()
#         query = queryset(user=self.request.user)
#         return query

class GetMyPost(APIView):
    permission_classes = [IsAuthenticated]
    @csrf_exempt
    def get(seft, request, *args, **kwargs):
        print(request.user.id)
        user = get_object_or_404(User, pk = request.user.id)
        query = Motel.objects.filter(user = user)
        print(query)
        serializer = MotelSerializer(query)
        return Response(serializer.data)


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
    serializer_class = GetMotelSerializer


class MotelUpdate(generics.UpdateAPIView): #Cập nhật bài đăng api/motels/update/<pk>
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Motel.objects.all()
    serializer_class = MotelSerializer

    def get_queryset(self): #Authentication user để update
        query = Motel.objects.filter(user=self.request.user)
        return query


class MotelDelete(generics.DestroyAPIView): #Xóa bài bài đăng api/motels/delete/<pk>/
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = GetMotelSerializer

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
