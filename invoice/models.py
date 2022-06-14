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
