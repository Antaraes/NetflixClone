from django.urls import path
from .views import signup,login,logout,MovieApi,UserApi,SignInView,RegisterView

urlpatterns = [
    # path('signup/',signup,name='signup'),
    path('login/',login,name='login'),
    path('signin/',SignInView.as_view(),name='signin'),
    path('signup/',RegisterView.as_view(),name='signup'),
    path('logout/',logout,name='logout'),
    path('movie/',MovieApi,name='Movie'),
]