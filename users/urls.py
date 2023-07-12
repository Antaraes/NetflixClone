from django.urls import path,re_path
from .views import (
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    LogoutView,
    CustomerProviderAuthView,
)
urlpatterns = [
    re_path(
        r'^o/(?P<provider>\S+)/$', CustomerProviderAuthView.as_view(), name='provider_auth'
    ),
    path('jwt/create/',CustomTokenObtainPairView.as_view()),
    path('jwt/refersh/',CustomTokenRefreshView.as_view()),
    path('jwt/verify/',CustomTokenVerifyView.as_view()),
    path('logout/',LogoutView.as_view())
]
