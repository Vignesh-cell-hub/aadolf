from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="dashboard_index"),
    #path('upload/',views.upload,name="upload")
]
