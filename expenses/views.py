from django.shortcuts import render,redirect,get_object_or_404
from .models import Expenses
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    alldetails = Expenses.objects.filter(organisation=request.user.profile.organisation)
    context = {"alldetails":alldetails}
    return render(request,'expenses/expense_tbl.html',context)

@login_required
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
                        expense_file = expense_file,
                        organisation=request.user.profile.organisation)

        expense.save()
        return redirect(index)
    return render(request,'expenses/expenses.html')

@login_required
def editexpense(request,id):
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

        expense = Expenses.objects.get(id=id)

        expense.expense_date=expense_date
        expense.expense_account=expense_account
        expense.expense_type=expense_type
        expense.expense_sac=expense_sac
        expense.expense_amount=expense_amount
        expense.expense_paid=expense_paid
        expense.expense_vendor=expense_vendor
        expense.expense_gst=expense_gst
        expense.expense_destination=expense_destination
        expense.expense_rev_charge=expense_rev_charge
        expense.expense_tax=expense_tax
        expense.expense_invoice=expense_invoice
        expense.expense_notes=expense_notes
        expense.customer_name=customer_name
        expense.expense_file=expense_file

        expense.save()
        return redirect(index)
    else:
        expense = get_object_or_404(Expenses, pk=id)
        context = {
            'expense': expense
        }
        print("customer edit html invoked")
        return render(request, 'expenses/expense_edit.html', context)