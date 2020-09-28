from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="paymentrec_index"),
    path('upload/',views.upload,name='paymentrec_upload')
    
]
