from django.shortcuts import render
from .models import Stovyklaviete, Privalumas

def index(request):
    top_stovyklavietes = Stovyklaviete.objects.order_by('-reitingas')[:5]
    return render(request, 'stovyklavietes/index.html', {'top_stovyklavietes': top_stovyklavietes})

def add_stovyklaviete(request):
    if request.method == 'POST':
        pavadinimas = request.POST['pavadinimas']
        reitingas = int(request.POST['reitingas'])
        stovyklaviete = Stovyklaviete.objects.create(pavadinimas=pavadinimas, reitingas=reitingas)

        privalumai = request.POST.getlist('privalumai')
        for privalumas in privalumai:
            Privalumas.objects.create(pavadinimas=privalumas, stovyklaviete=stovyklaviete)

    return render(request, 'stovyklavietes/add_stovyklaviete.html')

def info(request):
    return render(request, 'stovyklavietes/info.html')

def about(request):
    return render(request, 'stovyklavietes/about.html')
