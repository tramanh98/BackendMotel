from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from .views import *

app_name = 'motel'

# router = routers.DefaultRouter()
# router.register(r'posts', views.PhongTroListCreateAPIView)
# router.register(r'posts', views.PhongTroUpdateDeleteAPIView, basename="Posts")
urlpatterns = [
    # url('^api/', include(router.urls)),
    path('uploadimg/', ImgUpload.as_view()),
    path('api/getmypost', GetMyPost.as_view()),
    path('api/motels/', MotelList.as_view()), #Sort list
    path('api/motels/create/', CreateMotelViews.as_view()), #Post method
    path('api/motels/get/<pk>/', MotelDetail.as_view()), #Get method
    path('api/motels/put/<pk>/', MotelUpdate.as_view()), #Update method
    path('api/motels/delete/<pk>/', MotelDelete.as_view()), #Delete method
    path('api/motels/upload', MotelList.as_view()), #Upload photo
    path('api/motels/latest', MotelListLatest.as_view()), # Get list latest
]
# urlpatterns += [
#     path('api-auth/', include('rest_framework.urls')),
# ]