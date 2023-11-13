# serializers.py
from rest_framework import serializers
from .models import UserDriver

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDriver
        fields = '__all__'
