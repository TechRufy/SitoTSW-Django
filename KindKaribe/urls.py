from django.urls import path
from . import views


app_name = 'KindKaribe'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('Pasticceria/', views.Catalogo.as_view(), name="Pasticceria"),
    path('Gelateria/', views.CatalogoG.as_view(), name="Gelateria"),
    path('Carrello/', views.Carrello, name="Carrello"),
    path('AggiungiCarrello/',views.Aggiungi, name="aggiungiCarrello")
]
