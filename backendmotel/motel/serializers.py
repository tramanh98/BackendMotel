
from rest_framework import serializers

from rest_framework import serializers
from .models import Motel, ImageMotel
import json
from user.models import User
import datetime


class ImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk', read_only=True)

    class Meta:
        model = ImageMotel
        fields = ('id','motel', 'image')


class MotelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk', read_only=True)
    class Meta:
        model = Motel
        fields = ('id', 'title', 'content', 'typeMotel', 'address', 'ward',
                  'district', 'phone_number',
                  'arc', 'price')
