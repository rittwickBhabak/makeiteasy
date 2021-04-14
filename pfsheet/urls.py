from django.urls import path
from pfsheet import views

urlpatterns = [
    path('', views.home, name='home'),
    path('calculate', views.calculate, name='calculate'),
    path('result', views.result, name='result'),
]
