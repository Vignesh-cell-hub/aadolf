from django.shortcuts import render,redirect
from customer.models import Customer
from itemform.models import Item
from django.http import HttpResponse,JsonResponse
from .models import Estimate,Estimate_transaction
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    details = Estimate.objects.filter(organisation=request.user.profile.organisation.organisation_name)
    return render(request, "estimates/estimate_tbl.html",{"details":details})

@login_required
def upload(request):
    alldetails = Customer.objects.filter(organisation=request.user.profile.organisation.organisation_name)
    allitems = Item.objects.filter(organisation=request.user.profile.organisation.organisation_name)
    if request.method == 'POST':
        customer_name = Customer.objects.get(pk=request.POST['customer_name']).company_name
        billingStreet = request.POST['billing0']
        billingCity = request.POST['billing1']
        billingState = request.POST['billing2']
        billingZipcode = request.POST['billing3']
        shippingStreet = request.POST['shipping0']
        shippingCity = request.POST['shipping1']
        shippingState = request.POST['shipping2']
        shippingZipcode = request.POST['shipping3']
        projectname = request.POST['projectname']
        salesperson = request.POST['salesperson']
        subtotal = request.POST['subtotal']
        cgst = request.POST['cgst']
        sgst = request.POST['sgst']
        discount = request.POST['showdiscount']
        adjustment = request.POST['showadjustment']
        #total = request.POST['total']
        customernotes = request.POST['customernotes']
        terms = request.POST['terms']
        estimate = request.POST['estimate']
        reference = request.POST['reference']
        estimate_date = request.POST['estimate_date']
        expiry_date = request.POST['expiry_date']

        user = Estimate(estimate_date=estimate_date, estimate=estimate, reference=reference, customer_name=customer_name,
                        expiry_date=expiry_date, billingStreet=billingStreet, billingCity=billingCity,
                       billingState=billingState, billingZipcode=billingZipcode,
                       shippingStreet=shippingStreet, shippingCity=shippingCity, shippingState=shippingState,
                       shippingZipcode=shippingZipcode, project_name=projectname, sales_person=salesperson,
                       sub_total=subtotal, cgst=cgst, sgst=sgst,organisation=request.user.profile.organisation.organisation_name,
                       discount=discount, adjustments=adjustment, customer_notes=customernotes,
                       terms_condition=terms)
        user.save()

        for obj in range(1, 3):
            item_details = request.POST['name' + str(obj)]
            quantity = request.POST['quantity' + str(obj)]
            rate = request.POST['rate' + str(obj)]
            tax = request.POST['gst' + str(obj)]
            amount = request.POST['amount' + str(obj)]
            final = Estimate_transaction(item_details=item_details, quantity=quantity, rate=rate, tax=tax, amount=amount,
                                        invoice=user)
            final.save()

        return redirect(index)
    else:
        count = len(Estimate.objects.all())
        if count > 0:
            last_record = Estimate.objects.last()
            next_num = last_record.id + 1
        else:
            next_num = 1
        print("next", next_num)
        context = {"alldetails": alldetails, 'items': allitems, 'next_number': next_num}
    return render(request, "estimates/estimate_form.html", context)

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