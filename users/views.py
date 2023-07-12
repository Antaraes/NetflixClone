from django.shortcuts import render
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from djoser.social.views import ProviderAuthView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
class CustomerProviderAuthView(ProviderAuthView):
    def post(self,request,*args, **kwargs):
        reponse = super().post(request,*args, **kwargs)
        if reponse.status_code == 201:
            access_token=reponse.data.get('access')
            refresh_token=reponse.data.get('refresh')
            reponse.set_cookie(
                'access',
                access_token,
                max_age=settings.AUTH_COOKIE_ACCESS_MAX_AGE,
                path=settings.AUTH_COOKIE_PATH,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE
            )
            reponse.set_cookie(
                'refresh',
                refresh_token,
                max_age=settings.AUTH_COOKIE_REFERSH_MAX_AGE,
                path=settings.AUTH_COOKIE_PATH,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE
            )
        return reponse

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self,request,*args, **kwargs):
        reponse = super().post(request,*args, **kwargs)
        if reponse.status_code == 200:
            access_token = reponse.data.get('access')
            refersh_token = reponse.data.get('refresh')
            reponse.set_cookie(
                'access',
                access_token,
                max_age=settings.AUTH_COOKIE_ACCESS_MAX_AGE,
                path=settings.AUTH_COOKIE_PATH,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE
            )
            reponse.set_cookie(
                'refresh',
                refersh_token,
                max_age=settings.AUTH_COOKIE_REFERSH_MAX_AGE,
                path=settings.AUTH_COOKIE_PATH,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE
            )
        return reponse
    
class CustomTokenRefreshView(TokenRefreshView):
    def post(self,request,*args, **kwargs):
        refersh_token = request.COOKIES.get('refresh')
        if refersh_token:
            request.data['refresh'] = refersh_token
        reponse= super().post(request,*args, **kwargs)
        if reponse.status_code == 200:
            access_token=reponse.data.get('access')
            reponse.set_cookie(
                'access',
                access_token,
                max_age=settings.AUTH_COOKIE_ACCESS_MAX_AGE,
                path=settings.AUTH_COOKIE_PATH,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE
            )
        return reponse

class CustomTokenVerifyView(TokenVerifyView):
    def post(self,request,*args, **kwargs):
        access_token=request.COOKIES.get('access')
        if access_token:
            request.data['token']=access_token 
        return super().post(request,*args, **kwargs)
# Create your views here.

class LogoutView(APIView):
    def post(self,request,*args, **kwargs):
        reponse = Response(status=status.HTTP_204_NO_CONTENT)
        reponse.delete_cookie('access')
        reponse.delete_cookie('refresh')
        return reponse