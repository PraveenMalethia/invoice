from django.urls import path
from . import views


urlpatterns = [
    path("", views.Home, name="Home"),
    path("create-invoice", views.CreateInvoice, name="create-invoice"),
    path("create-customer", views.CreateCustomer, name="create-customer"),
    path("invoice-details/<int:id>/", views.InvoiceDetails, name="invoice-detail"),
    path("invoice-pdf/<int:id>/", views.InvoicePDF, name="invoice-pdf"),
]
