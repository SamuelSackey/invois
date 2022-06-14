from django.urls import path
from . import views

app_name = 'invoice'

urlpatterns = [
    path('', views.index, name="index"),
    path('add_business', views.add_business, name="add_business"),
    path('create_invoice', views.create_invoice, name="create_invoice"),
    path('<int:invoice_id>/edit_invoice',
         views.edit_invoice, name="edit_invoice"),
    path('<int:invoice_id>/add_item', views.add_item, name="add_item"),
    path('<int:invoice_id>/delete_item/<int:item_id>',
         views.delete_item, name="delete_item"),
]
