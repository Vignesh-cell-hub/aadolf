from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="vendor_index"),
    path('upload/',views.upload,name="vendor_upload"),
    path('<int:id>',views.editvendor,name="edit_vendor"),
]
