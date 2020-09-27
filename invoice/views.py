from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from customer.models import Customer
from itemform.models import Item
from .models import Invoice
from django.core import serializers

# Create your views here.
def index(request):
    details = Invoice.objects.all()
    return render(request, "invoice/invoice_tbl.html",{"details":details})
def upload(request):
    alldetails = Customer.objects.all()
    allitems = Item.objects.all()
    

    if request.method == 'POST':
        invoice_date = request.POST['invoicedate']
        invoice = request.POST['invoice']
        order_no = request.POST['order_no']
        customer_name = Customer.objects.get(pk = request.POST['customer_name']).company_name
        due_date = request.POST['due_date']
        amount = request.POST['totalamount']
        sub_total = request.POST['sub_totalamount']
        user = Invoice(invoice_date = invoice_date,invoice = invoice, order_no = order_no, customer_name = customer_name, due_date=due_date,amount=amount, sub_total = sub_total,total = amount)
        user.save()
        return redirect(index)
    else:
        count = len(Invoice.objects.all())
        if count>0:
            last_record = Invoice.objects.last()
            next_num = last_record.id+1  
        else:
            next_num = 1
        print("next",next_num)   
        context = {"alldetails":alldetails,'items':allitems,'next_number':1}
    return render(request, "invoice/invoice_form.html",context)

def getdata(request,id):
    print("id :",id)
    current_user_data = Customer.objects.get(id=id)
    # current_user_data = current_user_datas[0]
    gst_treatment = current_user_data.gst_treatment
    
    billing_address = current_user_data.billing_address 
    billing_city = current_user_data.billing_city
    billing_state = current_user_data.billing_state
    billing_zipcode = current_user_data.billing_zipcode
    
    shipping_address = current_user_data.shipping_address
    shipping_city = current_user_data.shipping_city
    shipping_state = current_user_data.shipping_state
    shipping_zipcode = current_user_data.shipping_zipcode

    datas = {}
    datas['billing_address'] = billing_address+'<br>'+billing_city+"<br>"+billing_state+"<br>"+billing_zipcode
    datas['shipping_address'] = shipping_address+"<br>"+shipping_city+"<br>"+shipping_state+"<br>"+shipping_zipcode
    datas['wgst'] = gst_treatment
    return JsonResponse({'data':datas,'current_user_data':serializers.serialize('json', [current_user_data,])})