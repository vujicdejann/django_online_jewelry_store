from django.contrib import admin
from .models import Kategorija, Proizvod

@admin.register(Kategorija)
class KategorijaAdmin(admin.ModelAdmin):
    list_display = ['naziv', 'opis']
    search_fields = ['naziv', 'opis']

@admin.register(Proizvod)
class ProizvodAdmin(admin.ModelAdmin):
    list_display = ['id', 'naziv', 'cena', 'dostupnost', 'kategorija']
    list_filter = ['dostupnost', 'kategorija']
    search_fields = ['naziv', 'opis', 'kategorija__naziv']
