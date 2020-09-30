"""adolf_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('',include('dashboard.urls')),
    path('customer/',include('customer.urls')),
    path('itemform/',include('itemform.urls')),
    path('invoice/',include('invoice.urls')),
    path('estimate/',include('estimate.urls')),
    path('expenses/',include('expenses.urls')),
    path('vendor/',include('vendor.urls')),
    path('sales/',include('sales.urls')),
    path('bills/',include('bills.urls')),
    path('report/',include('report.urls')),
    path('delivery_challan/',include('delivery_challan.urls')),
    path('purchaseitem/',include('purchaseitem.urls')),
    path('paymentreceived/',include('paymentreceived.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
