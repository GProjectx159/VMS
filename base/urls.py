from django.urls import path, include
from . import views

urlpatterns = [
 path("", views.home, name="home"),
 path("signup/", views.sginup, name="sginup"),
 path('login/', views.loginUser, name='login'),
 path('logout/', views.logoutUser, name='logout'),
#  path("accounts/", include("django.contrib.auth.urls")),
]
