from django.shortcuts import render, redirect
from .forms import KontaktForma
from .models import Porudzbina, StavkaPorudzbine
from ProdavnicaNakita.models import Proizvod

def naruci(request):
    if request.method == 'POST':
        forma = KontaktForma(request.POST)
        if forma.is_valid():
            porudzbina = Porudzbina.objects.create(
                korisnik=request.user,
                ime=forma.cleaned_data['ime'],
                prezime=forma.cleaned_data['prezime'],
                email=forma.cleaned_data['email'],
                adresa=forma.cleaned_data['adresa'],
                grad=forma.cleaned_data['grad'],
                postanski_broj=forma.cleaned_data['postanski_broj'],
                dodatne_informacije=forma.cleaned_data['dodatne_informacije'],
            )
            korpa = request.session.get('korpa', {})
            for proizvod_id, kolicina in korpa.items():
                proizvod = Proizvod.objects.get(id=proizvod_id)
                StavkaPorudzbine.objects.create(
                    porudzbina=porudzbina,
                    proizvod=proizvod,
                    cena=proizvod.cena,
                    kolicina=kolicina
                )
            request.session['korpa'] = {}
            return redirect('detalji_porudzbine', porudzbina.id)
    else:
        forma = KontaktForma()
    return render(request, 'Porudzbina/naruci.html', {'forma': forma})

def detalji_porudzbine(request, id):
    porudzbina = Porudzbina.objects.get(id=id)
    stavke = porudzbina.stavke.all()

    ukupna_cena_porudzbine = 0
    for stavka in stavke:
        stavka.ukupna_cena_stavke = stavka.kolicina * stavka.cena
        ukupna_cena_porudzbine += stavka.ukupna_cena_stavke

    return render(request, 'Porudzbina/detalji_porudzbine.html', {
        'porudzbina': porudzbina,
        'stavke': stavke,
        'ukupna_cena_porudzbine': ukupna_cena_porudzbine
    })
