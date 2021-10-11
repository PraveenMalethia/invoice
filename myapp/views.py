from django.shortcuts import render , redirect
from .models import Customer, Invoice , Item
from django.http import HttpResponse
from django.views.generic import View

# pdf rendering imports
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.


def Home(request):
    context = {}
    template = "index.html"
    invoices = Invoice.objects.filter(customer__user=request.user)
    context['invoices'] = invoices
    return render(request, template, context)


def CreateInvoice(request):
    context = {}
    customers = Customer.objects.filter(user=request.user)
    context['customers'] = customers
    template = "CreateInvoice.html"
    if request.method == "POST":
        customer = Customer.objects.get(id=int(request.POST.get('customer')))
        price = int(request.POST.get('price'))
        description = request.POST.get('description')
        invoice = Invoice.objects.create(customer=customer , price=price , description=description)
        invoice.save()
        return redirect('/')
    return render(request,template,context)

def CreateCustomer(request):
    context = {}
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        customer = Customer.objects.create(user=request.user, name=name, phone=phone, email=email)
        customer.save()
        return redirect('/')
    template = "CreateCustomer.html"
    return render(request,template,context)

# view for rendering html to pdf files
def InvoiceDetails(request,id):
    context = {}
    template = "InvoiceDetails.html"
    invoice = Invoice.objects.get(id=id)
    context['invoice'] = invoice
    return render(request,template,context)

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def InvoicePDF(self, id):
    invoice = Invoice.objects.get(id=id)
    data = {
        'created': invoice.date_created, 
        'price': invoice.price,
        'customer': invoice.customer,
        'id': invoice.id,
    }
    pdf = render_to_pdf('InvoicePDF.html', data)
    return HttpResponse(pdf, content_type='application/pdf')