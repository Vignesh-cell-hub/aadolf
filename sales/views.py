from django.shortcuts import render,redirect
from customer.models import Customer
from django.http import HttpResponse,JsonResponse
from itemform.models import Item
from invoice.models import Invoice
from .models import Sales
from django.contrib.auth.decorators import login_required
from django.conf import settings
from accounts.models import Organisation

# Create your views here.
@login_required
def index(request):
    # details = Sales.objects.filter(organisation=request.user.profile.organisation.organisation_name)
    organisation=Organisation.objects.filter(organisation_name=request.user.profile.organisation.organisation_name)
    context={
            'organisation': organisation[0],
            'media_url': settings.MEDIA_URL,
        }
    return render(request, "sales/sales_tbl.html",context)

@login_required
def upload(request):
    alldetails = Customer.objects.filter(organisation=request.user.profile.organisation.organisation_name)
    allitems = Item.objects.filter(organisation=request.user.profile.organisation.organisation_name)
    organisation=Organisation.objects.filter(organisation_name=request.user.profile.organisation.organisation_name)

    context = {"alldetails":alldetails,'items':allitems,'organisation': organisation[0],'media_url': settings.MEDIA_URL,}

    if request.method == 'POST':
        sales_date = request.POST['sales_date']
        sales_order = request.POST['sales_order']
        reference = request.POST['reference']
        customer_name = Customer.objects.get(pk = request.POST['customer_name']).company_name
        shipment_date = request.POST['shipment_date']
        amount = request.POST['totalamount']

        user = Sales(sales_date = sales_date,sales_order = sales_order, reference = reference, customer_name = customer_name, shipment_date=shipment_date,amount=amount,organisation=request.user.profile.organisation.organisation_name)
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
        context = {"alldetails":alldetails,'items':allitems,'next_number':1,'organisation': organisation[0],'media_url': settings.MEDIA_URL,}
    
    return render(request,'sales/sales_form.html',context)

@login_required
def getdata(request,id):
    print("id :",id)
    current_user_data = Customer.objects.get(id=id)
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
    datas['gst'] = gst_treatment
    
    return JsonResponse({'data':datas})