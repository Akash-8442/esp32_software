from django.urls import path
from . import views

urlpatterns = [
    path('sensor_data/', views.sensor_data, name='sensor_data'),
    path('data_recieved/', views.data_recieved, name='data_recieved'),
    path('/', views.sensor_data, name='sensor_data')
]
