from django.urls import path
from .views import home_view  # Import the view you just created

urlpatterns = [
    path('', home_view, name='home'),  # Set the home_view function to the root URL
    path('reform/new/', reform_create_view, name='reform_create'),
    path('reform/<int:pk>/update/', reform_update_view, name='reform_update'),
    path('states/<str:state_name>/', views.StateReforms, name='state_reforms'),
]
