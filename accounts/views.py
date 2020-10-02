from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import auth
from django.conf import settings
from .models import Organisation

# Create your views here.

def loginuser(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            print("login")
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            else:
                return redirect("/")
        else:
            return render(request, 'accounts/loginpage.html',{'invalid':'invalid'})
    else:
        return render(request, 'accounts/loginpage.html')


def logoutuser(request):
    auth.logout(request)
    return render(request, 'accounts/loginpage.html')

def manage(request):
    if request.method == 'POST':
        organisation = Organisation.objects.get(id=request.user.profile.organisation.id)

        if 'img' in request.FILES:
            organisation_logo=request.FILES['img']
            if organisation_logo:
                organisation.organisation_logo = organisation_logo
        organisation_name=request.POST['name']
        industry=request.POST['industry']
        business_location=request.POST['business_locations']
        company_address1=request.POST['address1']
        company_address2=request.POST['address2']
        city=request.POST['city']
        state=request.POST['state']
        zipcode=request.POST['zipcode']
        ph_no=request.POST['phno']
        fax=request.POST['fax']
        website=request.POST['website']
        company_ID=request.POST['companyID']
        Tax_ID=request.POST['TaxID']


        organisation.organisation_name=organisation_name
        organisation.industry=industry
        organisation.business_location=business_location
        organisation.company_address1=company_address1
        organisation.company_address2=company_address2
        organisation.city=city
        organisation.state=state
        organisation.zipcode=zipcode
        organisation.ph_no=ph_no
        organisation.fax=fax
        organisation.website=website
        organisation.Company_ID=company_ID
        organisation.Tax_ID=Tax_ID

        organisation.save()
 
        return redirect('manage')

    else:
        organisation=Organisation.objects.filter(organisation_name=request.user.profile.organisation.organisation_name)

        context={
            'organisation': organisation[0],
            'media_url': settings.MEDIA_URL,
        }
        return render(request, 'organisation_profile.html',context)