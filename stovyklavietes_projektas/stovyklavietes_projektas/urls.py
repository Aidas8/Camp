from django.urls import path
# from .views import index, add_stovyklaviete, info, about
# from stovyklavietes_projektas.views import index, add_stovyklaviete, info, about
# from stovyklavietes_projektas.stovyklavietes.views import index, add_stovyklaviete, info, about
from .stovyklavietes.views import index, add_stovyklaviete, info, about

urlpatterns = [
    path('', index, name='index'),
    path('add_stovyklaviete/', add_stovyklaviete, name='add_stovyklaviete'),
    path('info/', info, name='info'),
    path('about/', about, name='about'),
]