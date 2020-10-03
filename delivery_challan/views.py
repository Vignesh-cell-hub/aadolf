from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
    return render(request,'delivery_challan/delivery_table.html')

def upload(request):
    return render(request, 'delivery_challan/delivery_form.html')


