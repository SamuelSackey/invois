from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.


@login_required
def index(request):

    has_business = Business.objects.filter(user=request.user)
    if not has_business:
        return redirect(reverse("invoice:add_business"))

    return redirect(reverse("invoice:create_invoice"))


@login_required
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


@login_required
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


@login_required
def edit_invoice(request, invoice_id):
    invoice = Invoice.objects.get(pk=invoice_id)

    if invoice.user == request.user:
        items = Item.objects.filter(invoice=invoice)

        # Total
        subtotal = 0
        for item in items:
            subtotal += item.total_cost()

        total = subtotal * (1 + invoice.tax/100)
        return render(request, "invoice/edit_invoice.html", {
            "invoice": invoice,
            "items": items,
            "total": total
        })

    return redirect(reverse("accounts:index"))


@login_required
def add_item(request, invoice_id):
    invoice = Invoice.objects.get(pk=invoice_id)

    if invoice.user == request.user:
        if request.method == "POST":
            name = request.POST["name"]
            quantity = request.POST["quantity"]
            price = request.POST["price"]

            item = Item(name=name, quantity=quantity,
                        price=price, invoice=invoice)
            item.save()

            return redirect(reverse("invoice:edit_invoice", args=(invoice.id,)))

        return render(request, "invoice/add_invoice.html", {
            "invoice": invoice
        })

    return redirect(reverse("accounts:index"))


@login_required
def delete_item(request, invoice_id, item_id):
    invoice = Invoice.objects.get(pk=invoice_id)

    if invoice.user == request.user:
        item = Item.objects.get(pk=item_id)
        item.delete()

        return redirect(reverse("invoice:edit_invoice", args=(invoice.id,)))

    return redirect(reverse("accounts:index"))
