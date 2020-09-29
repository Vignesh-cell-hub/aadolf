from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="estimate_index"),
    path('getdata/<int:id>/',views.getdata,name="getdata"),
    path('upload/',views.upload,name="upload")
]
