from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from .views import *

app_name = 'motel'

urlpatterns = [
    path('api/user/motel', GetAllPost.as_view()), # Get all user's post and user's infor
    path('api/motels/', MotelList.as_view()), # Sort list
    path('api/motels/create/', CreateMotelViews.as_view()), # Post method
    path('api/motels/get/<pk>/', MotelDetail.as_view()), # Get method
    path('api/motels/put/<int:id>/', MotelUpdate.as_view()), # Update method
    path('api/motels/delete/<pk>/', MotelDelete.as_view()), # Delete method
    path('api/motels/img/upload/', PhotoUploadView.as_view()), # Upload photo
    path('api/motels/img/delete/<int:img_fk>/<pk>/', PhotoMotelDelete.as_view()), # Xóa ảnh của bài đăng
    path('api/motels/latest', MotelListLatest.as_view()), # Get list latest
]