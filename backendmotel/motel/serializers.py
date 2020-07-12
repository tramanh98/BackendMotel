
from rest_framework import serializers

from rest_framework import serializers
from .models import Motel, ImageMotel
import json
from user.models import User
from user.serializers import  UserSerializer
import datetime


# Để đăng ảnh của phòng trọ
class PhotoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk', read_only=True)
    class Meta:
        model = ImageMotel
        fields = ('id','motel', 'image')


class GetImageSerializer(serializers.ModelSerializer): # kết hợp với MotelSerializer để lấy bài đăng cùng hình ảnh, 
                                                        # không dùng để đăng ảnh phòng trọ
    id = serializers.IntegerField(source='pk', read_only=True)
    class Meta:
        model = ImageMotel
        fields = ('id','image')

class MotelSerializer(serializers.ModelSerializer): # để get, create, update, delete bài đăng 
    images = GetImageSerializer(many=True, required = False)
    id = serializers.IntegerField(source='pk', read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Motel
        fields = ('id', 'user', 'title', 'content', 'typeMotel', 'address', 'ward',
                  'district', 'local_map', 'phone_number', 'arc', 'price', 'created_at', 'updated_at', 'images')
        read_only_fields = ('created_at', 'updated_at')
        


class GetMotelSerializer(serializers.ModelSerializer):  # kết hợp với UserMotelSerializers để lấy các bài đăng của user
                                                        # không dùng để đăng bài 
    id = serializers.IntegerField(source='pk', read_only=True)
    class Meta:
        model = Motel
        fields = ('id', 'title', 'content', 'typeMotel', 'address', 'ward',
                  'district', 'local_map', 'phone_number', 'arc', 'price', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

class UserMotelSerializers(serializers.ModelSerializer):
    post = GetMotelSerializer(many=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name','phone','email', 'post')
