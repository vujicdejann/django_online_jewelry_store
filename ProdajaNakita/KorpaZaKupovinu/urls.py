from django.urls import path
from . import views

urlpatterns = [
    path('dodaj/<int:proizvod_id>/', views.dodaj_u_korpu, name='dodaj_u_korpu'),
    path('prikazi/', views.prikazi_korpu, name='prikazi_korpu'),
    path('ukloni/<int:proizvod_id>/', views.ukloni_iz_korpe, name='ukloni_iz_korpe'),
    path('azuriraj/<int:proizvod_id>/<int:kolicina>/', views.azuriraj_korpu, name='azuriraj_korpu'),
]
