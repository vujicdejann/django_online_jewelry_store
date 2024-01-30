from django.db import models
from django.conf import settings
from ProdavnicaNakita.models import Proizvod

class Porudzbina(models.Model):
    korisnik = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ime = models.CharField(max_length=100)
    prezime = models.CharField(max_length=100)
    email = models.EmailField()
    adresa = models.CharField(max_length=255)
    grad = models.CharField(max_length=100)
    postanski_broj = models.CharField(max_length=20)
    placeno = models.BooleanField(default=False)
    kreirano = models.DateTimeField(auto_now_add=True)
    azurirano = models.DateTimeField(auto_now=True)
    dodatne_informacije = models.TextField(blank=True)


    class Meta:
        ordering = ('-kreirano',)

    def __str__(self):
        return f'Porudzbina {self.id}'

class StavkaPorudzbine(models.Model):
    porudzbina = models.ForeignKey(Porudzbina, related_name='stavke', on_delete=models.CASCADE)
    proizvod = models.ForeignKey(Proizvod, related_name='stavke_porudzbina', on_delete=models.CASCADE)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    kolicina = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
