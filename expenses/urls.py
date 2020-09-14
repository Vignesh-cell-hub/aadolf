from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="expense_index"),
    path('upload/',views.upload,name="expense_upload"),
    path('<int:id>',views.editexpense,name="edit_expense"),
]
