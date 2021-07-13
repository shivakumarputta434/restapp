from rest_framework import serializers
from .models import Company

class Company_Serializer(serializers.ModelSerializer):

    class Meta:
        model=Company
        fields = '__all__'

    def create(self, validated_data):
        return Company.objects.create(**validated_data)
