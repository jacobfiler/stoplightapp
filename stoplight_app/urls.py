from .views import home_view  # Import the view you just created
from .views import reform_list

urlpatterns = [
    path('', views.home, name='home_default'), 
    path('<str:data_version>/', views.home, name='home'),
    path('states/<str:state_name>/', views.StateReforms, name='state_reforms'),
    path('reform_detail/<str:slcid>/', views.reform_detail, name='reform_detail'),
    path('oauth2/', include('django_auth_adfs.urls')),

]
