from django.contrib import admin
from .models import Porudzbina, StavkaPorudzbine

class StavkaPorudzbineInline(admin.TabularInline):
    model = StavkaPorudzbine
    raw_id_fields = ['proizvod']

@admin.register(Porudzbina)
class PorudzbinaAdmin(admin.ModelAdmin):
    list_display = ['ime', 'prezime', 'email', 'adresa', 'placeno', 'kreirano', 'azurirano']
    list_filter = ['placeno', 'kreirano', 'azurirano']
    inlines = [StavkaPorudzbineInline]

