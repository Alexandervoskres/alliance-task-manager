from django.urls import path

from . import views


app_name = 'inventory_ai'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('sample.csv', views.sample_csv, name='sample_csv'),
]

