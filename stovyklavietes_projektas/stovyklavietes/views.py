from django.shortcuts import render, redirect
from .models import Stovyklaviete, Privalumas

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

        return redirect('index')

    return render(request, 'stovyklavietes/add_stovyklaviete.html')