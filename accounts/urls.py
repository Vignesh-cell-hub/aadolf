from django.urls import path,include
from . import views

urlpatterns = [
    path('login/',views.loginuser,name='loginuser'),
    path('logout/',views.logoutuser,name='logoutuser')

]