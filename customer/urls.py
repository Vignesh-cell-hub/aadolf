from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name="customer_index"),
    path('upload/', views.upload, name="customer_upload"),
    path('<int:id>', views.editcustomer, name="edit_customer"),
]
