from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from stoplight_app import views

urlpatterns = [
    path('admin/login/', lambda request: redirect('django_auth_adfs:login')),  # Redirect to Azure SSO login
    path('admin/', admin.site.urls),  # Keep the admin panel accessible
    path('', views.home, name='home_default'), 
    path('<str:data_version>/', views.home, name='home'),
    path('states/<str:state_name>/', views.StateReforms, name='state_reforms'),
    path('states/<str:state_name>/<str:slcid>/', views.state_reform_detail, name='state_reform_detail'),
    path('reform_detail/<str:slcid>/', views.reform_detail, name='reform_detail'),
    path('oauth2/', include('django_auth_adfs.urls')),  # SSO URL patterns
]
