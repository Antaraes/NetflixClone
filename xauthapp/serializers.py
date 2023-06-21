from rest_framework import  serializers
from .models import Movie,Account
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password, check_password
class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate(self, data):
        password1 = data.get('password1')
        password2 = data.get('password2')
        if password1 and password2 and password1 != password2:
            raise serializers.ValidationError("Passwords don't match")
        return data
    def create(self, validated_data):
        user = UserCreationForm(data=validated_data)
        if user.is_valid():
            user.save()
            return user
        else:
            raise serializers.ValidationError(user.errors)
    class Meta:
        model = User
        fields = ('email','username','password1','password2')

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Account
        fields = ('email','username','password')
    def create(self, validated_data):
        password = validated_data.pop('password')
        hashed_password = make_password(password)
        account = Account.objects.create(password=hashed_password, **validated_data)
        return account

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title','type','price')