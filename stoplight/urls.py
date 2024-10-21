"""
URL configuration for stoplight project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from stoplight_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home_default'), 
    path('<str:data_version>/', views.home, name='home'),
    path('states/<str:state_name>/', views.StateReforms, name='state_reforms'),
    path('states/<str:state_name>/<str:slcid>/', views.state_reform_detail, name='state_reform_detail'),
    path('reform_detail/<str:slcid>/', views.reform_detail, name='reform_detail'),
    path('oauth2/', include('django_auth_adfs.urls')),

    
]
