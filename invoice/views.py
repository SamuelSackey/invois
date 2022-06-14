from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "invoice/index.html")


def add_business(request):
    return render(request, "invoice/add_business.html")
