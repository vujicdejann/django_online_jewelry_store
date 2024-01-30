from django.shortcuts import render, redirect, get_object_or_404
from .models import StavkaKorpe
from ProdavnicaNakita.models import Proizvod
from django.views.decorators.http import require_POST

@require_POST
def dodaj_u_korpu(request, proizvod_id):
    korpa = request.session.get('korpa', {})
    kolicina = int(request.POST.get('kolicina', 1))
    if proizvod_id not in korpa:
        korpa[proizvod_id] = kolicina
    else:
        korpa[proizvod_id] += kolicina
    request.session['korpa'] = korpa
    return redirect('prikazi_korpu')

def prikazi_korpu(request):
    korpa = request.session.get('korpa', {})
    proizvodi = Proizvod.objects.filter(id__in=korpa.keys())
    stavke_korpe = []
    for proizvod in proizvodi:
        stavke_korpe.append({
            'proizvod': proizvod,
            'kolicina': korpa[str(proizvod.id)]
        })
    return render(request, 'KorpaZaKupovinu/prikazi_korpu.html', {'stavke_korpe': stavke_korpe})

def ukloni_iz_korpe(request, proizvod_id):
    korpa = request.session.get('korpa', {})
    if str(proizvod_id) in korpa:
        del korpa[str(proizvod_id)]
        request.session['korpa'] = korpa
    return redirect('prikazi_korpu')

@require_POST
def azuriraj_korpu(request):
    korpa = request.session.get('korpa', {})
    for key, value in request.POST.items():
        if key.startswith('kolicina_'):
            proizvod_id = key.split('_')[1]
            korpa[proizvod_id] = int(value)
    request.session['korpa'] = korpa
    return redirect('prikazi_korpu')

def prikazi_korpu(request):
    korpa = request.session.get('korpa', {})
    proizvodi = Proizvod.objects.filter(id__in=korpa.keys())
    stavke_korpe = []
    ukupna_cena = 0
    for proizvod in proizvodi:
        kolicina = korpa[str(proizvod.id)]
        cena = proizvod.cena * kolicina
        ukupna_cena += cena
        stavke_korpe.append({
            'proizvod': proizvod,
            'kolicina': kolicina,
            'cena': cena
        })
    return render(request, 'KorpaZaKupovinu/prikazi_korpu.html', {'stavke_korpe': stavke_korpe, 'ukupna_cena': ukupna_cena})
