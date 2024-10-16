from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout

# model
from user_auth.models import CustomUser


class LoginView(View):

    def get(self, request, *args, **kwargs):

        return render(request, "auth/login.html")

    def post(self, request, *args, **kwargs):

        email = request.POST.get("email", None)
        password = request.POST.get("password", None)

        user = authenticate(request, email=email, password=password)
        if not user:
            messages.error(request, "email or Password does not exist.")
            return redirect("login-view")
        login(request, user)
        return redirect("home-view")


@method_decorator(login_required(login_url="login-view"), name="dispatch")
class LogOutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("login-view")


class RegisterView(View):

    def get(self, request, *args, **kwargs):

        return render(request, "auth/register.html")

    def post(self, request, *args, **kwargs):

        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
        re_password = request.POST.get("re-password", None)

        # Validate password length
        if password and len(password) < 8:
            messages.error(request, "Password must be at least 8 characters long.")
            return redirect("register-view")

        if password != re_password:
            return redirect("register")

        customer_obj = CustomUser.objects.create(email=email)
        customer_obj.set_password(password)
        customer_obj.save()

        return redirect("login-view")


@method_decorator(login_required(login_url="login-view"), name="dispatch")
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home.html")
