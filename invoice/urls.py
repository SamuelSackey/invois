from django.urls import path
from . import views

app_name = 'invoice'

urlpatterns = [
    path('', views.index, name="index"),
    path('add_business', views.add_business, name="add_business"),
    path('create_invoice', views.create_invoice, name="create_invoice"),
    path('<int:invoice_id>/invoice', views.invoice, name="invoice"),
]
