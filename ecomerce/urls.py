"""
URL configuration for ecomerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('cooks.urls')),
    path('registerapp/', include('registerapp.urls')),
    path('Servicesapp/', include('Servicesapp.urls')),
    # path('payapp/',include('payapp.urls')),
    path('paymentapp/',include('paymentapp.urls')),
    # path('news/', views.news_list, name='news_list'),

    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
