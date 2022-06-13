from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return redirect(reverse("accounts:login"))

    return render(request, "accounts/home.html")


def login_view(request):
    return render(request, "accounts/login.html")


def register_view(request):
    return render(request, "accounts/register.html")


def logout_view(request):
    return render(request, "accounts/home.html")
