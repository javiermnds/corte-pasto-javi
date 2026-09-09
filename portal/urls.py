from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('trabajos/', views.trabajo, name='trabajo'),
]