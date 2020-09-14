from django.shortcuts import render,redirect,get_object_or_404
from .models import Vendor
#from django.http import HttpResponse
# Create your views here.
def index(request):
    alldetails = Vendor.objects.all()
    context = {"alldetails":alldetails}
    return render(request,'vendor/vendor_tbl.html',context)
def upload(request):
    if request.method == 'POST':
        primarycontact = request.POST['primarycontact']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        company_name = request.POST['companyname']
        display_name = request.POST['customerdisplayname']
        email = request.POST['customeremail']
        work_phone_no = request.POST['Workphone']
        mobile_phone_no = request.POST['mobile']
        website = request.POST['website']

        gst_treatment = request.POST['gsttreatment']
        source_of_supply = request.POST['place_of_supply']
        currency = request.POST['currency']
        opening_balance = request.POST['openingbalance']
        payment_terms = request.POST['paymentterms']
        tds = request.POST['tds']
        facebook = request.POST['facebook']
        twitter = request.POST['twitter']

        billing_attention = request.POST['billattention']
        billing_country = request.POST['billCountry']
        billing_address = request.POST['billaddress']
        billing_city = request.POST['billcity']
        billing_state = request.POST['billstate']
        billing_zipcode = request.POST['billzipc']
        billing_phone = request.POST['billphone']
        billing_fax = request.POST['billfax']

        shipping_attention = request.POST['attention']
        shipping_country = request.POST['Country']
        shipping_address = request.POST['address']
        shipping_city = request.POST['city']
        shipping_state = request.POST['state']
        shipping_zipcode = request.POST['zipc']
        shipping_phone = request.POST['phone']
        shipping_fax = request.POST['fax']

        user = Vendor(primarycontact = primarycontact,
                    first_name = first_name,
                    last_name = last_name,
                    company_name = company_name,
                    display_name = display_name,
                    email = email,
                    work_phone_no = work_phone_no,
                    mobile_phone_no = mobile_phone_no,
                    website = website,

                    gst_treatment = gst_treatment,
                    source_of_supply = source_of_supply,
                    currency = currency,
                    opening_balance = opening_balance,
                    payment_terms = payment_terms,
                    tds = tds,
                    facebook=facebook,
                    twitter = twitter,

                    billing_attention=billing_attention,
                    billing_country=billing_country,
                    billing_address=billing_address,
                    billing_city=billing_city,
                    billing_state=billing_state,
                    billing_zipcode=billing_zipcode,
                    billing_phone=billing_phone,
                    billing_fax=billing_fax,

                    shipping_attention =shipping_attention,
                    shipping_country =shipping_country,
                    shipping_address =shipping_address,
                    shipping_city =shipping_city,
                    shipping_state =shipping_state,
                    shipping_zipcode =shipping_zipcode,
                    shipping_phone =shipping_phone,
                    shipping_fax =shipping_fax,
                    )
        user.save()
        return redirect(index)
    else:print('get request')
    return render(request,'vendor/vendor_form.html')


def editvendor(request,id):
    if request.method == 'POST':
        primarycontact = request.POST['primarycontact']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        company_name = request.POST['companyname']
        display_name = request.POST['customerdisplayname']
        email = request.POST['customeremail']
        work_phone_no = request.POST['Workphone']
        mobile_phone_no = request.POST['mobile']
        website = request.POST['website']

        gst_treatment = request.POST['gsttreatment']
        source_of_supply = request.POST['place_of_supply']
        currency = request.POST['currency']
        opening_balance = request.POST['openingbalance']
        payment_terms = request.POST['paymentterms']
        tds = request.POST['tds']
        facebook = request.POST['facebook']
        twitter = request.POST['twitter']

        billing_attention = request.POST['billattention']
        billing_country = request.POST['billCountry']
        billing_address = request.POST['billaddress']
        billing_city = request.POST['billcity']
        billing_state = request.POST['billstate']
        billing_zipcode = request.POST['billzipc']
        billing_phone = request.POST['billphone']
        billing_fax = request.POST['billfax']

        shipping_attention = request.POST['attention']
        shipping_country = request.POST['Country']
        shipping_address = request.POST['address']
        shipping_city = request.POST['city']
        shipping_state = request.POST['state']
        shipping_zipcode = request.POST['zipc']
        shipping_phone = request.POST['phone']
        shipping_fax = request.POST['fax']

        customer= Vendor.objects.get(id=id)


        customer.primarycontact = primarycontact
        customer.first_name = first_name
        customer.last_name =last_name
        customer.company_name = company_name
        customer.display_name = display_name
        customer.email = email
        customer.work_phone_no = work_phone_no
        customer.mobile_phone_no = mobile_phone_no
        customer.website = website

        customer.gst_treatment = gst_treatment
        customer.source_of_supply = source_of_supply
        customer.currency = currency
        customer.opening_balance = opening_balance
        customer.payment_terms =payment_terms
        customer.tds = tds
        customer.facebook = facebook
        customer.twitter = twitter

        customer.billing_attention =billing_attention
        customer.billing_country =billing_country
        customer.billing_address = billing_address
        customer.billing_state = billing_state
        customer.billing_city=billing_city
        customer.billing_zipcode = billing_zipcode
        customer.billing_phone =billing_phone
        customer.billing_fax = billing_fax

        customer.shipping_attention = shipping_attention
        customer.shipping_country = shipping_country
        customer.shipping_address =shipping_address
        customer.shipping_city = shipping_city
        customer.shipping_state = shipping_state
        customer.shipping_zipcode =shipping_zipcode
        customer.shipping_phone = shipping_phone
        customer.shipping_fax =shipping_fax
        customer.save()
        return redirect('vendor_index')

    else:
        customer=get_object_or_404(Vendor,pk=id)
        context={
            'customer':customer
        }
        print("vendor edit html invoked")
        return render(request,'vendor/vendor_edit.html',context)