from django.shortcuts import render,redirect
from .models import Expenses

# Create your views here.
def index(request):
    alldetails = Expenses.objects.all()
    context = {"alldetails":alldetails}
    return render(request,'expenses/expense_tbl.html',context)
def upload(request):
    if request.method == 'POST':
        expense_date = request.POST['date']
        expense_account = request.POST['Exp_Account']
        expense_type = request.POST['customRadioInline1']
        expense_sac = request.POST['SAC']
        expense_amount = request.POST['amount']
        expense_paid = request.POST['paid']
        expense_vendor = request.POST['vendor']
        expense_gst = request.POST['gstd']
        expense_destination = request.POST['des_supply']
        expense_rev_charge = request.POST.get('rev_charge', False)
        expense_tax = request.POST['tax']
        expense_invoice = request.POST['invoice']
        expense_notes = request.POST['notes']
        customer_name = request.POST['custom_name']
        expense_file = request.POST['expensefile']


        expense = Expenses(expense_date = expense_date,
                        expense_account = expense_account,
                        expense_type = expense_type,
                        expense_sac = expense_sac,
                        expense_amount = expense_amount,
                        expense_paid = expense_paid,
                        expense_vendor = expense_vendor,
                        expense_gst = expense_gst,
                        expense_destination = expense_destination,
                        expense_rev_charge = expense_rev_charge,
                        expense_tax = expense_tax,
                        expense_invoice = expense_invoice,
                        expense_notes = expense_notes,
                        customer_name = customer_name,
                        expense_file = expense_file)

        expense.save()
        return redirect(index)
    return render(request,'expenses/expenses.html')