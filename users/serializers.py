from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'




class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()