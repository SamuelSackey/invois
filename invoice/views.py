from django.urls import reverse
from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def index(request):

    has_business = Business.objects.filter(user=request.user)
    if not has_business:
        return redirect(reverse("invoice:add_business"))

    return redirect(reverse("invoice:create_invoice"))


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

        return redirect(reverse("invoice:index"))

    return render(request, "invoice/add_business.html")


def create_invoice(request):
    if request.method == "POST":
        title = request.POST["title"]
        issue_date = request.POST["issue_date"]
        tax = request.POST["tax"]

        invoice = Invoice(title=title, issue_date=issue_date,
                          tax=tax, user=request.user)
        invoice.save()

        return redirect(reverse("invoice:edit_invoice", args=(invoice.id,)))

    has_business = Business.objects.filter(user=request.user)
    if not has_business:
        return redirect(reverse("invoice:add_business"))

    return render(request, "invoice/create_invoice.html")


def edit_invoice(request, invoice_id):
    invoice = Invoice.objects.get(pk=invoice_id)

    if invoice.user == request.user:
        items = Item.objects.filter(invoice=invoice)
        return render(request, "invoice/edit_invoice.html", {
            "invoice": invoice,
            "items": items
        })

    return redirect(reverse("accounts:index"))
