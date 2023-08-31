from django.urls import path
from stovyklavietes.views import pagrindinis, add_stovyklaviete, info, about

urlpatterns = [
    path('', pagrindinis, name='pagrindinis'),
    path('add_stovyklaviete/', add_stovyklaviete, name='add_stovyklaviete'),
    path('info/', info, name='info'),
    path('about/', about, name='about'),
]