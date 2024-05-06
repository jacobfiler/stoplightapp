from .views import home_view  # Import the view you just created
from .views import reform_list

urlpatterns = [
    path('', home_view, name='home'),  # Set the home_view function to the root URL
    path('states/<str:state_name>/', views.StateReforms, name='state_reforms'),
    path('reform_detail/<str:slcid>/', views.reform_detail, name='reform_detail'),
    path('oauth2/', include('django_auth_adfs.urls')),

]
