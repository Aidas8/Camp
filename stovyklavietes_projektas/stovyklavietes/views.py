from django.shortcuts import render, redirect
from .models import Stovyklaviete, Privalumas

def pagrindinis(request):
    stovyklavietes = Stovyklaviete.objects.all()
    return render(request, 'stovyklavietes/pagrindinis.html', {'stovyklavietes': stovyklavietes})

def add_stovyklaviete(request):
    if request.method == 'POST':
        pavadinimas = request.POST['pavadinimas']
        reitingas = int(request.POST['reitingas'])
        koordinates = request.POST['koordinates']
        nuotrauka = request.FILES.get('nuotrauka')
        papildoma_info = request.POST['papildoma_info']

        stovyklaviete = Stovyklaviete.objects.create(pavadinimas=pavadinimas, reitingas=reitingas, koordinates=koordinates, nuotrauka=nuotrauka, papildoma_info=papildoma_info)

        privalumai = request.POST.getlist('privalumai')
        for privalumas in privalumai:
            Privalumas.objects.create(pavadinimas=privalumas, stovyklaviete=stovyklaviete)

        return redirect('pagrindinis')

    return render(request, 'stovyklavietes/add_stovyklaviete.html')

def info(request):
    return render(request, 'stovyklavietes/info.html')

def about(request):
    return render(request, 'stovyklavietes/about.html')