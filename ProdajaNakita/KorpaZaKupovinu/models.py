from django.db import models
from django.conf import settings
from ProdavnicaNakita.models import Proizvod

class StavkaKorpe(models.Model):
    korisnik = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    proizvod = models.ForeignKey(Proizvod, on_delete=models.CASCADE)
    kolicina = models.IntegerField(default=1)
    kreirano = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('kreirano',)

    def __str__(self):
        return f'{self.kolicina} x {self.proizvod.naziv}'

    def ukupna_cena(self):
        return self.kolicina * self.proizvod.cena


