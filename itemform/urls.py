from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="itemform_index"),
    path('<int:item_id>',views.editItem,name="editItem"),
    path('upload/',views.upload,name="upload")
]
