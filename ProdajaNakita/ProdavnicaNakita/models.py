from django.db import models

from django.db import models

class Kategorija(models.Model):
    naziv = models.CharField(max_length=100)
    opis = models.TextField()

    def __str__(self):
        return self.naziv

class Proizvod(models.Model):
    naziv = models.CharField(max_length=100)
    opis = models.TextField()
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    dostupnost = models.BooleanField(default=True)
    kategorija = models.ForeignKey(Kategorija, on_delete=models.CASCADE)
    slika = models.ImageField(upload_to='proizvodi_slike/', blank=True, null=True)

    def __str__(self):
        return self.naziv

