from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from django.contrib.auth.decorators import login_required


# from django.http import HttpResponse
# Create your views here.
@login_required
def index(request):
    print(request.user)
    alldetails = Customer.objects.filter(organisation=request.user.profile.organisation.organisation_name)
    context = {"alldetails": alldetails}
    return render(request, 'customer/customer_tbl.html', context)

@login_required
def upload(request):
    if request.method == 'POST':
        print('hi')
        customer_type = request.POST['type']
        primarycontact = request.POST['primarycontact']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        company_name = request.POST['companyname']
        display_name = request.POST['displayname']
        email = request.POST['customeremail']
        work_phone_no = request.POST['Workphone']
        mobile_phone_no = request.POST['mobile']
        # designation = request.POST['designation']
        # dept = request.POST['dept']
        website = request.POST['website']
 
        gst_treatment = request.POST['gsttreatment']
        place_of_supply = request.POST['place of supply']
        tax_prefrence = request.POST['taxtype']
        currency = request.POST['currency']
        # opening_balance = request.POST['openingbalance']
        payment_terms = request.POST['paymentterms']
        # enable_portal = request.POST.get('yes', False)
        # portal_language = request.POST['potallanguage']
        # facebook = request.POST['facebook']
        # twitter = request.POST['twitter']

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

        user = Customer(customer_type=customer_type,
                        primarycontact=primarycontact,
                        first_name=first_name,
                        last_name=last_name,
                        company_name=company_name,
                        display_name=display_name,
                        email=email,
                        work_phone_no=work_phone_no,
                        mobile_phone_no=mobile_phone_no,
                        # designation=designation,
                        # dept=dept,
                        website=website,

                        gst_treatment=gst_treatment,
                        place_of_supply=place_of_supply,
                        tax_prefrence=tax_prefrence,
                        currency=currency,
                        # opening_balance=opening_balance,
                        payment_terms=payment_terms,
                        # enable_portal=enable_portal,
                        # portal_language=portal_language,
                        # facebook=facebook,
                        # twitter=twitter,

                        billing_attention=billing_attention,
                        billing_country=billing_country,
                        billing_address=billing_address,
                        billing_city=billing_city,
                        billing_state=billing_state,
                        billing_zipcode=billing_zipcode,
                        billing_phone=billing_phone,
                        billing_fax=billing_fax,

                        shipping_attention=shipping_attention,
                        shipping_country=shipping_country,
                        shipping_address=shipping_address,
                        shipping_city=shipping_city,
                        shipping_state=shipping_state,
                        shipping_zipcode=shipping_zipcode,
                        shipping_phone=shipping_phone,
                        shipping_fax=shipping_fax,
                        organisation=request.user.profile.organisation.organisation_name,
                        )
        user.save()
        return redirect(index)
    else:
        print('get request')

    return render(request, 'customer/customer_form.html')

@login_required
def editcustomer(request, id):
    if request.method == 'POST':
        customer_type = request.POST['type']
        primarycontact = request.POST['primarycontact']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        company_name = request.POST['companyname']
        display_name = primarycontact + " " + first_name + " " + last_name
        email = request.POST['customeremail']
        work_phone_no = request.POST['Workphone']
        mobile_phone_no = request.POST['mobile']
        # designation = request.POST['designation']
        # dept = request.POST['dept']
        website = request.POST['website']

        gst_treatment = request.POST['gsttreatment']
        place_of_supply = request.POST['place of supply']
        tax_prefrence = request.POST['taxtype']
        currency = request.POST['currency']
        # opening_balance = request.POST['openingbalance']
        payment_terms = request.POST['paymentterms']
        # enable_portal = request.POST.get('yes', False)
        # portal_language = request.POST['potallanguage']
        # facebook = request.POST['facebook']
        # twitter = request.POST['twitter']

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

        customer = Customer.objects.get(id=id)

        customer.customer_type = customer_type
        customer.primarycontact = primarycontact
        customer.first_name = first_name
        customer.last_name = last_name
        customer.company_name = company_name
        customer.display_name = display_name
        customer.email = email
        customer.work_phone_no = work_phone_no
        customer.mobile_phone_no = mobile_phone_no
        # customer.designation = designation
        # customer.dept = dept
        customer.website = website

        customer.gst_treatment = gst_treatment
        customer.place_of_supply = place_of_supply
        customer.tax_prefrence = tax_prefrence
        customer.currency = currency
        # customer.opening_balance = opening_balance
        customer.payment_terms = payment_terms
        # customer.enable_portal = enable_portal
        # customer.portal_language = portal_language
        # customer.facebook = facebook
        # customer.twitter = twitter

        customer.billing_attention = billing_attention
        customer.billing_country = billing_country
        customer.billing_address = billing_address
        customer.billing_state = billing_state
        customer.billing_city = billing_city
        customer.billing_zipcode = billing_zipcode
        customer.billing_phone = billing_phone
        customer.billing_fax = billing_fax

        customer.shipping_attention = shipping_attention
        customer.shipping_country = shipping_country
        customer.shipping_address = shipping_address
        customer.shipping_city = shipping_city
        customer.shipping_state = shipping_state
        customer.shipping_zipcode = shipping_zipcode
        customer.shipping_phone = shipping_phone
        customer.shipping_fax = shipping_fax
        customer.save()
        return redirect('customer_index')

    else:
        customer = get_object_or_404(Customer, pk=id)
        context = {
            'customer': customer
        }
        print("customer edit html invoked")
        return render(request, 'customer/customer_edit.html', context)