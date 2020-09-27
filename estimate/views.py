from django.shortcuts import render,redirect
from customer.models import Customer
from itemform.models import Item
from django.http import HttpResponse,JsonResponse
from .models import Estimate
from invoice.models import Invoice

# Create your views here.
def index(request):
    details = Estimate.objects.all()
    return render(request, "estimates/estimate_tbl.html",{"details":details})
def upload(request):
    alldetails = Customer.objects.all()
    allitems = Item.objects.all()
    context = {"alldetails":alldetails,'items':allitems}

    if request.method == 'POST':
        estimate_date = request.POST['estimate_date']
        estimate_number = request.POST['estimate']
        ref_number = request.POST['reference']
        customer_name = Customer.objects.get(pk = request.POST['customer_name']).company_name
        estimate_amount = request.POST['total']

        user = Estimate(estimate_date = estimate_date,estimate_number = estimate_number, ref_number = ref_number, customer_name = customer_name, estimate_amount=estimate_amount)
        user.save()
        return redirect(index)
    return render(request, "estimates/estimate_form.html",context)


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