from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializers): #for getting and posting data about user
    class Meta:
        model = get_user_model() 
        fields = ['id', 'username', 'email', 'phone_number', 'bio', 'profile_picture']

class RegisterSerializers(serializers.ModelSerializers):
    model = get_user_model()
    fields = ['username', 'email', 'password', 'phone_number', 'bio', 'profile_picture']
    extra_kwargs = {
            'password': {'write_only': True},
        }
    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data) #for hashing password
        return user
