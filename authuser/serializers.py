from rest_framework import serializers
from .models import UserCustom

class UserCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCustom
        fields = ['id', 'username','email', 'password','level']  # Sesuaikan dengan bidang yang Anda inginkan
