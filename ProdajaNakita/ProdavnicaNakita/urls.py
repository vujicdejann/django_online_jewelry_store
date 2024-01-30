from django.urls import path
from . import views

urlpatterns = [
    path('proizvodi/', views.lista_proizvoda, name='lista_proizvoda'),
    path('proizvod/<int:id>/', views.detalji_proizvoda, name='detalji_proizvoda'),
]
