from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Business(models.Model):
    name = models.CharField(max_length=128)
    contact = models.IntegerField()
    address = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    country = models.CharField(max_length=64)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="businesses"
    )

    def __str__(self):
        return f"{self.name} | {self.contact} | {self.country} "


class Invoice(models.Model):
    title = models.CharField(max_length=128)
    issue_date = models.DateField()
    tax = models.IntegerField(default=0)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="invoices"
    )

    def __str__(self):
        return f"{self.title} | {self.issue_date} | {self.tax}% "


class Item(models.Model):
    name = models.CharField(max_length=128)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.CASCADE,
        related_name="items"
    )

    def __str__(self):
        return f"{self.name} | qty: {self.quantity} | ${self.price} "
