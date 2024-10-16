# myapp/urls.py
from django.urls import path
from user_auth.views import HomeView, LoginView, RegisterView, LogOutView

urlpatterns = [
    path("", HomeView.as_view(), name="home-view"),
    path("login/", LoginView.as_view(), name="login-view"),
    path("logout/", LogOutView.as_view(), name="logout-view"),
    path("register/", RegisterView.as_view(), name="register-view"),
]
