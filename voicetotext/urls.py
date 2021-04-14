from django.urls import path
from voicetotext import views

urlpatterns = [
    path('', views.home, name='home'),
]
