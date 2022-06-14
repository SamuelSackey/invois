from django.urls import reverse
from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def index(request):
    has_business = Business.objects.filter(user=request.user)

    if not has_business:
        return redirect(reverse("invoice:add_business"))

    return render(request, "invoice/index.html")


def add_business(request):
    if request.method == "POST":
        name = request.POST["name"]
        contact = request.POST["contact"]
        address = request.POST["address"]
        city = request.POST["city"]
        country = request.POST["country"]

        business = Business(name=name, contact=contact, address=address,
                            city=city, country=country, user=request.user)
        business.save()
        print(business)

        return redirect(reverse("invoice:index"))

    return render(request, "invoice/add_business.html")
