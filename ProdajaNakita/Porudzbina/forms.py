from django import forms

class KontaktForma(forms.Form):
    ime = forms.CharField(label='Ime', max_length=100)
    prezime = forms.CharField(label='Prezime', max_length=100)
    email = forms.EmailField(label='Email')
    adresa = forms.CharField(label='Adresa', max_length=300)
    grad = forms.CharField(label='Grad', max_length=100)
    postanski_broj = forms.CharField(label='Poštanski broj', max_length=20)
    dodatne_informacije = forms.CharField(widget=forms.Textarea, required=False)
