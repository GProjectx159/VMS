from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path("Home/", views.home_after, name="home_after"),
    path("signup/", views.sginup, name="sginup"),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
#   path("accounts/", include("django.contrib.auth.urls")),

    path('reset_password/', views.CustomPasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='registration/reset_password_sent.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/reset.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/reset_password_complete.html'), name='password_reset_complete'),
]
