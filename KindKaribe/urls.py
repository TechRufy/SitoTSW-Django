from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('Pasticceria', views.Catalogo.as_view(), name="CatalogoPasticceria")
]
