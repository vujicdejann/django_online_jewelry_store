from django.shortcuts import render, get_object_or_404
from .models import Proizvod

def lista_proizvoda(request):
    proizvodi = Proizvod.objects.all()
    return render(request, 'ProdavnicaNakita/lista_proizvoda.html', {'proizvodi': proizvodi})

def detalji_proizvoda(request, id):
    proizvod = get_object_or_404(Proizvod, id=id)
    return render(request, 'ProdavnicaNakita/detalji_proizvoda.html', {'proizvod': proizvod})

