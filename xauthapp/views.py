from django.shortcuts import render
from django.views.decorators import csrf
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http.response import JsonResponse
from .serializers import UserSerializer,MovieSerializer,AccountSerializer
from .models import Account,Movie
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
import pymongo
@csrf_exempt
def signup(request):
    if request.method == "POST":
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Success", safe=False)
        return JsonResponse("Failed to Add", safe=False)

@csrf_exempt
def UserApi(request):
    if request.method == "POST":
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Success", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == "GET":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse("Successfully")
        return JsonResponse({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=400)

class SignInView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = Account.objects.get(email=email)
            hashed_password = check_password(password,user.password)
            if hashed_password:
                return Response({'message': 'Sign in successful.'})
            else:
                return Response({'error': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)
        except ObjectDoesNotExist:
            return Response({'error': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)

class RegisterView(APIView):
    def post(self,request):
        try:
            user_data = JSONParser().parse(request)
            user_serializer = AccountSerializer(data=user_data)
            if user_serializer.is_valid():
                user_serializer.save()
                return JsonResponse("Added Success", safe=False)
            return JsonResponse("Failed to Add", safe=False)
        except ObjectDoesNotExist:
            return Response({'error': 'Invalid.'}, status=status.HTTP_401_UNAUTHORIZED)
@api_view(['POST'])
def logout(request):
    if request.user.is_authenticated:
        logout(request)
        return Response(status=status.HTTP_200_OK)
    return Response({'error': 'User not logged in'}, status=status.HTTP_401_UNAUTHORIZED)

@csrf_exempt
def MovieApi(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        movies_serializer = MovieSerializer(movies,many=True)
        return JsonResponse(movies_serializer.data,safe=False)
    elif request.method == 'POST':
        movie_data = JSONParser().parse(request)
        movies_serializer = MovieSerializer(data=movie_data)
        if movies_serializer.is_valid():
            movies_serializer.save()
            return JsonResponse("Added Success",safe=False)
        return JsonResponse("Failed to Add",safe=False)