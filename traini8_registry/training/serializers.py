# training/serializers.py
from rest_framework import serializers
from .models import TrainingCenter, Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class TrainingCenterSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = TrainingCenter
        fields = '__all__'

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        
        address, created = Address.objects.get_or_create(**address_data)
        
        training_center = TrainingCenter.objects.create(address=address, **validated_data)
        return training_center