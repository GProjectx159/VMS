from django.urls import path
from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("Home/", views.home_after, name="home_after"),
    path("signup/", views.sginup, name="sginup"),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
#  path("accounts/", include("django.contrib.auth.urls")),

]
