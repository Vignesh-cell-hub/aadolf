from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from customer.models import Customer
from itemform.models import Item
from .models import Invoice,Invoice_transaction
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.conf import settings
from accounts.models import Organisation

 
# Create your views here.
@login_required
def index(request):
    # details = Invoice.objects.filter(organisation=request.user.profile.organisation.organisation_name)
    organisation=Organisation.objects.filter(organisation_name=request.user.profile.organisation.organisation_name)

    context={
            'organisation': organisation[0],
            'media_url': settings.MEDIA_URL,
        }
    return render(request, "invoice/invoice_tbl.html",context)

@login_required
def upload(request):
    alldetails = Customer.objects.filter(organisation=request.user.profile.organisation.organisation_name)
    allitems = Item.objects.filter(organisation=request.user.profile.organisation.organisation_name)
    organisation=Organisation.objects.filter(organisation_name=request.user.profile.organisation.organisation_name)


    if request.method == 'POST':
        customer_name = Customer.objects.get(pk = request.POST['customer_name']).company_name
        billingStreet=request.POST['billing0']
        billingCity=request.POST['billing1']
        billingState=request.POST['billing2']
        billingZipcode=request.POST['billing3']
        shippingStreet =request.POST['shipping0']
        shippingCity =request.POST['shipping1']
        shippingState =request.POST['shipping2']
        shippingZipcode =request.POST['shipping3']
        placeofsupply=request.POST['placeofsupply']
        salesperson=request.POST['salesperson']
        subtotal=request.POST['subtotal']
        cgst=request.POST['cgst']
        sgst=request.POST['sgst']
        igst=request.POST['igst']
        discount=request.POST['showdiscount']
        adjustment=request.POST['showadjustment']
        total=request.POST['total']
        customernotes=request.POST['customernotes']
        terms=request.POST['terms']
        invoice=request.POST['invoice']
        order_no=request.POST['order_no']
        invoice_date=request.POST['invoicedate']
        due_date=request.POST['due_date']
        print("Row Count : ",request.POST['rowcount'])
        user = Invoice(invoice_date = invoice_date,invoice = invoice, order_no = order_no, customer_name = customer_name, due_date=due_date,billingStreet=billingStreet,billingCity=billingCity,billingState=billingState,billingZipcode=billingZipcode,
                       shippingStreet=shippingStreet,shippingCity=shippingCity,shippingState=shippingState,shippingZipcode=shippingZipcode,place_of_supply=placeofsupply,sales_person=salesperson,sub_total=subtotal,cgst=cgst,sgst=sgst,igst=igst,
                       discount=discount,adjustments=adjustment,total=total,customer_notes=customernotes,terms_condition=terms,organisation=request.user.profile.organisation.organisation_name)
        user.save()

        for obj in range(1,2):
            item_details = request.POST['name' + str(obj)]
            quantity = request.POST['quantity' + str(obj)]
            rate = request.POST['rate' + str(obj)]
            tax = request.POST['gst' + str(obj)]
            amount = request.POST['amount' + str(obj)]
            final = Invoice_transaction(item_details=item_details, quantity=quantity, rate=rate, tax=tax, amount=amount,invoice=user)
            final.save()
        if 'saveaspdf' in request.POST:
            print('saveaspdf')
            print(request.user.profile.organisation.organisation_name)
            context={
                'organisation':request.user.profile.organisation,
                'invoice':user,
                'invoice_transaction':Invoice_transaction.objects.filter(invoice=user),
                'organisation': organisation[0],
                'media_url': settings.MEDIA_URL,

            }
            return render(request, "invoice/pdfclone.html", context)
        elif 'save' in request.POST:
            print('save')
            return redirect(index)

    else:
        count = len(Invoice.objects.all())
        if count>0:
            last_record = Invoice.objects.last()
            next_num = last_record.id+1  
        else:
            next_num = 1
        print("next",next_num)   
        context = {"alldetails":alldetails,'items':allitems,'next_number':next_num,'organisation': organisation[0],'media_url': settings.MEDIA_URL,}
    return render(request, "invoice/invoice_form.html",context)


@login_required()
def printpdf(request,id):
    print(id)
    invoice=Invoice.objects.get(id=id)
    context = {
        'organisation': request.user.profile.organisation,
        'invoice': invoice ,
        'invoice_transaction': Invoice_transaction.objects.filter(invoice=invoice),
        'media_url': settings.MEDIA_URL,

    }
    return render(request, "invoice/pdfclone.html", context)

@login_required
def getdata(request,id):
    print("id :",id)
    current_user_data = Customer.objects.get(id=id)
    # current_user_data = current_user_datas[0]
    gst_treatment = current_user_data.gst_treatment
    gst_id = current_user_data.gst_id

    
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
    datas['wgst'] = gst_treatment+"<br>"+gst_id
    return JsonResponse({'data':datas,'current_user_data':serializers.serialize('json', [current_user_data,])})