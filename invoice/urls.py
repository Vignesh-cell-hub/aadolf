from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="invoice_index"),
    path('getdata/<int:id>/',views.getdata,name="getdata"),
    path('upload/',views.upload,name="upload"),
    path('<int:id>',views.printpdf, name="printpdf")
]
