from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login

from invoice.models import Invoice

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return redirect(reverse("accounts:login"))

    return redirect("accounts:home")


def home(request):
    invoices = Invoice.objects.filter(user=request.user)

    return render(request, "accounts/home.html", {
        "invoices": invoices
    })


def user(request):
    business = request.user.businesses.all().first()
    return render(request, "accounts/user.html", {
        "business": business
    })


def login_view(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse("accounts:index"))

        else:
            return render(request, "accounts/login.html", {
                "message": "Invalid credentials"
            })

    return render(request, "accounts/login.html")


def register_view(request):

    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 != password2:
            return render(request, "accounts/register.html", {
                "message": "Passwords not Matching"
            })

        elif User.objects.filter(username=username).exists():
            return render(request, "accounts/register.html", {
                "message": "Username Taken"
            })

        elif User.objects.filter(email=email).exists():
            return render(request, "accounts/register.html", {
                "message": "Email Taken"
            })

        else:
            user = User.objects.create_user(
                username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
            user.save()
            print("User Created")
            return redirect(reverse("accounts:index"))

    return render(request, "accounts/register.html")


def logout_view(request):
    logout(request)
    return render(request, "accounts/login.html", {
        "message": "Logged out"
    })
