
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



class GetImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk', read_only=True)

    class Meta:
        model = ImageMotel
        fields = ('id','image')

class GetMotelSerializer(serializers.ModelSerializer):
    motel = GetImageSerializer(many=True)
    id = serializers.IntegerField(source='pk', read_only=True)
    class Meta:
        model = Motel
        fields = ('id', 'title', 'content', 'typeMotel', 'address', 'ward',
                  'district', 'phone_number', 'arc', 'price', 'created_at', 'motel')

    def create(self, validated_data):
        arrimages = validated_data.pop('image')
        motel = super(GetMotelSerializer, self).create(**validated_data)
        for image in arrimages:
            ImageMotel.objects.create(motel = motel, image = image)
        return motel

class MotelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk', read_only=True)
    class Meta:
        model = Motel
        fields = ('id', 'title', 'content', 'typeMotel', 'address', 'ward',
                  'district', 'phone_number',
                  'arc', 'price', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')
