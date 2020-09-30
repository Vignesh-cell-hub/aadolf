from django.shortcuts import render,redirect,get_object_or_404
from .models import Item
from django.contrib.auth.decorators import login_required
from django.conf import settings
from accounts.models import Organisation

@login_required
def index(request):
    alldetails = Item.objects.filter(organisation=request.user.profile.organisation.organisation_name)
    organisation=Organisation.objects.filter(organisation_name=request.user.profile.organisation.organisation_name)

    context = {"alldetails":alldetails,
    'organisation': organisation[0],
            'media_url': settings.MEDIA_URL,
    }
    return render(request,'tables.html',context)
 
@login_required
def upload(request):
    organisation=Organisation.objects.filter(organisation_name=request.user.profile.organisation.organisation_name)

    context={
            'organisation': organisation[0],
            'media_url': settings.MEDIA_URL,
        }
    if request.method=='POST':
        item_type = request.POST['type']
        name = request.POST['name']
        units = request.POST['units']
        hsncode = request.POST['hsncode']
        taxpreference = request.POST['tax-preference']
        sellamount = request.POST['sellamount']
        salesacc = request.POST['salesacc']
        salesdes = request.POST['salesdes']
        puramount = request.POST['puramount']
        purchaseacc = request.POST['purchaseacc']
        purchasedes = request.POST['purchasedes'] 
        intrastate = request.POST['intrastate']
        interstate = request.POST['interstate']
    

        user = Item(item_type = item_type,
                    name = name,
                    units = units, 
                    hsncode = hsncode, 
                    taxpreference = taxpreference,
                    sellamount = sellamount,
                    salesacc = salesacc,
                    salesdes = salesdes,
                    puramount = puramount, 
                    purchaseacc = purchaseacc, 
                    purchasedes = purchasedes,
                    intrastate = intrastate,
                    interstate = interstate,organisation=request.user.profile.organisation.organisation_name)
        user.save()
        return redirect(index)
        
    else:
        pass
    return render(request,'items_form.html', context)

@login_required
def editItem(request,item_id):
    if request.method == 'POST':
        item_type = request.POST['type']
        name = request.POST['name']
        units = request.POST['units']
        hsncode = request.POST['hsncode']
        taxpreference = request.POST['tax-preference']
        sellamount = request.POST['sellamount']
        salesacc = request.POST['salesacc']
        salesdes = request.POST['salesdes']
        puramount = request.POST['puramount']
        purchaseacc = request.POST['purchaseacc']
        purchasedes = request.POST['purchasedes']
        intrastate = request.POST['intrastate']
        interstate = request.POST['interstate']

        item =Item.objects.get(id=item_id)
        item.item_type=item_type
        item.name=name
        item.units=units
        item.hsncode=hsncode
        item.taxpreference=taxpreference
        item.sellamount=sellamount
        item.salesacc=salesacc
        item.salesdes=salesdes
        item.puramount=puramount
        item.purchaseacc=purchaseacc
        item.purchasedes=purchasedes
        item.intrastate=intrastate
        item.interstate=interstate
        item.save()
        return redirect('itemform_index')
    else:
        item=get_object_or_404(Item,pk=item_id)
        context={
            'item':item
        }
        return render(request, 'update_item.html',context)