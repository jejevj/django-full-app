# serializers.py
from rest_framework import serializers,generics
from .models import UserDriver, UserCustomer, Delivery

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDriver
        fields = '__all__'


class UserDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDriver
        fields = '__all__'

class UserCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCustomer
        fields = '__all__'

class DeliveryCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'


class DriverUpdateView(generics.RetrieveUpdateAPIView):
    queryset = UserDriver.objects.all()
    serializer_class = UserDriverSerializer