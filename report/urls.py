from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('table/',views.table,name="table"),
    path('sales_by_items/',views.sales_by_items,name="sales_by_items"),
    path('expenses_details/',views.expenses_details,name="expenses_details"),
    path('sales_order_details/',views.sales_order_details,name="sales_order_details"),
    path('payment_received/',views.payment_received,name="payment_received"),
    path('vendor_balances/',views.vendor_balances,name="vendor_balances"),
    path('payment_made/',views.payment_made,name="payment_made"),
    path('purchases_order_details/',views.purchases_order_details,name="purchases_order_details"),
    path('purchases_by_vendor/',views.purchases_by_vendor,name="purchases_by_vendor"),
    path('purchases_by_item/',views.purchases_by_item,name="purchases_by_item"),
    
    
    
]
