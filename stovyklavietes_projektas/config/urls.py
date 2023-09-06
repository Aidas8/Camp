from django.urls import path
from stovyklavietes.views import pagrindinis, add_stovyklaviete, info, about, search_stovyklavietes
from stovyklavietes import views

urlpatterns = [
    path('', pagrindinis, name='pagrindinis'),
    path('add_stovyklaviete/', add_stovyklaviete, name='add_stovyklaviete'),
    path('info/', info, name='info'),
    path('about/', about, name='about'),
    path('search/', views.search_stovyklavietes, name='search_stovyklavietes'),
]