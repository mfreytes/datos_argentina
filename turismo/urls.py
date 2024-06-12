from django.urls import path, include
from turismo import views

urlpatterns = [
    path('', views.graficar),
]
