from django.urls import path
from . import views

urlpatterns = [
    path('naruci/', views.naruci, name='naruci'),
    path('detalji/<int:id>/', views.detalji_porudzbine, name='detalji_porudzbine'),

]
