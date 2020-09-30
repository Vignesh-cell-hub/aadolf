from django.shortcuts import render
from customer.models import Customer
from itemform.models import Item
from invoice.models import Invoice
from sales.models import Sales
from django.contrib.auth.decorators import login_required
from vendor.models import Vendor
from expenses.models import Expenses
from django.conf import settings
from accounts.models import Organisation



@login_required
def index(request):
    organisation=Organisation.objects.filter(organisation_name=request.user.profile.organisation.organisation_name)

    context={
            'organisation': organisation[0],
            'media_url': settings.MEDIA_URL,
        }
    return render(request,"report/index.html", context)

@login_required
def purchases_by_vendor(request):
    organisation=Organisation.objects.filter(organisation_name=request.user.profile.organisation.organisation_name)
    all_vendor = Vendor.objects.all() 
    vendor_data = []
    final_calc = {
        'expense_count':0 ,
        'bill_count' : 0,
        'total' : 0
    }
    for i in all_vendor:
        temp_customer = {}
        name = i.display_name
        temp_customer['name'] = name
        expense_list = Expenses.objects.filter(expense_vendor = name)
        temp_customer['expense_count'] = len(expense_list)
        temp_customer['bill_count'] = 0
        final_calc['expense_count']+=len(expense_list)
        final_calc['bill_count']=0
        temp_total = 0
        for expense in expense_list:
            temp_total += int(expense.expense_amount)
        temp_customer['total'] = temp_total
        final_calc['total'] +=temp_total
        vendor_data.append(temp_customer)

    context={
            'organisation': organisation[0],
            'media_url': settings.MEDIA_URL,
        }
    return render(request,"report/purchases_by_vendor.html",{'vendor_data':vendor_data,'final':final_calc}, context)

@login_required
def purchases_by_item(request):
    organisation=Organisation.objects.filter(organisation_name=request.user.profile.organisation.organisation_name)

    context={
            'organisation': organisation[0],
            'media_url': settings.MEDIA_URL,
        }
    return render(request,"report/purchases_by_item.html", context)

@login_required
def expenses_details(request):
    organisation=Organisation.objects.filter(organisation_name=request.user.profile.organisation.organisation_name)

    context={
            'organisation': organisation[0],
            'media_url': settings.MEDIA_URL,
        }
    all_expense = Invoice.objects.all()
    final_calc = {
        'total':0
    }
    temp_total = 0
    for i in all_expense:
        temp_total += i.total
    final_calc['total'] = temp_total

    return render(request,"report/expense_details.html",{'all_expense':all_expense,'final':final_calc}, context)

@login_required
def purchases_order_details(request):
    organisation=Organisation.objects.filter(organisation_name=request.user.profile.organisation.organisation_name)

    context={
            'organisation': organisation[0],
            'media_url': settings.MEDIA_URL,
        }
    return render(request,"report/purchaseorderdetails.html", context)

@login_required
def payment_made(request):
    organisation=Organisation.objects.filter(organisation_name=request.user.profile.organisation.organisation_name)

    context={
            'organisation': organisation[0],
            'media_url': settings.MEDIA_URL,
        }
    return render(request,"report/payment_made.html", context)

@login_required
def sales_order_details(request):
    organisation=Organisation.objects.filter(organisation_name=request.user.profile.organisation.organisation_name)

    context={
            'organisation': organisation[0],
            'media_url': settings.MEDIA_URL,
        }
    all_sales = Sales.objects.all()
    final_calc = {
        'total':0
    }
    temp_total = 0
    for i in all_sales:
        temp_total += i.total
    final_calc['total'] = temp_total

    return render(request,"report/sales_order_details.html",{'all_sales':all_sales,'final':final_calc}, context)

@login_required
def vendor_balances(request):
    organisation=Organisation.objects.filter(organisation_name=request.user.profile.organisation.organisation_name)

    context={
            'organisation': organisation[0],
            'media_url': settings.MEDIA_URL,
        }
    return render(request,"report/vendor_balances.html", context)
@login_required
def payment_received(request):
    organisation=Organisation.objects.filter(organisation_name=request.user.profile.organisation.organisation_name)

    context={
            'organisation': organisation[0],
            'media_url': settings.MEDIA_URL,
        }
    return render(request,"report/payment_received.html", context)

@login_required
def sales_by_items(request):
    organisation=Organisation.objects.filter(organisation_name=request.user.profile.organisation.organisation_name)

    context={
            'organisation': organisation[0],
            'media_url': settings.MEDIA_URL,
        }
    all_items = Item.objects.all() 
    invoice_data_item = []
    for item in all_items:
        temp_item = {}
        name = item.name
        sellamount = item.sellamount
        temp_item['name'] = name
        temp_item['sellamount'] = sellamount

        #invoice_list = Invoice.objects.filter(item_details = name)
        invoice_data_item.append(temp_item)

    return render(request,"report/sales_by_item.html", {'invoice_data_item':invoice_data_item}, context)

@login_required
def table(request):
    organisation=Organisation.objects.filter(organisation_name=request.user.profile.organisation.organisation_name)

    context={
            'organisation': organisation[0],
            'media_url': settings.MEDIA_URL,
        }
    all_customers = Customer.objects.all() 
    invoice_data = []
    final_calc = {
        'count':0 ,
        'subtotal':0, 
        'total':0
    }
    for customer in all_customers:
        temp_customer = {}
        name = customer.company_name
        temp_customer['name'] = name
        invoice_list = Invoice.objects.filter(customer_name = name)
        temp_customer['count'] = len(invoice_list)
        final_calc['count']+=len(invoice_list)
        temp_subtotal = 0 
        temp_total = 0
        for invoice in invoice_list:
            temp_subtotal += invoice.subtotal 
            temp_total += invoice.total 
        temp_customer['subtotal'] = temp_subtotal 
        final_calc['subtotal'] += temp_subtotal 
        final_calc['total'] +=temp_total
        temp_customer['total'] = temp_total 
        invoice_data.append(temp_customer)

    return render(request,'report/form.html',{'invoice_data':invoice_data,'final':final_calc}, context)