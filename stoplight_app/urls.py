from .views import home_view  # Import the view you just created
from .views import reform_list

urlpatterns = [
    path('', home_view, name='home'),  # Set the home_view function to the root URL
    path('reform/new/', reform_create_view, name='reform_create'),
    path('reform/<int:pk>/update/', reform_update_view, name='reform_update'),
     path('reform_status/<int:pk>/', reform_status_detail, name='reform_status_detail'),
    path('states/<str:state_name>/', views.StateReforms, name='state_reforms'),
    path('reforms/', reform_list, name='reform_list'),
    path('reform_area/', reform_area_list, name='reform_area_list'),
    path('reform_area/<int:pk>/', reform_area_detail, name='reform_area_detail'),
    path('states/', state_list, name='state_list'),
    path('oauth2/', include('django_auth_adfs.urls')),

]
