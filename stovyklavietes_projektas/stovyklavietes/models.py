from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

REGIONAI = (
    ('Aukstaitija', 'Aukštaitija'),
    ('Dzukija', 'Dzūkija'),
    ('Suvalkija', 'Suvalkija'),
    ('Zemaitija', 'Žemaitija'),
)

class Stovyklaviete(models.Model):
    pavadinimas = models.CharField(max_length=100)
    reitingas = models.PositiveIntegerField(                 #reitingavimo kodas
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
        ]
    )
    koordinates = models.CharField(max_length=50, blank=True, null=True)  #prideja "blank" ir "null=true" galime palikti tuscia lauka
    nuotrauka = models.ImageField(upload_to='stovyklavietes/', blank=True, null=True)
    papildoma_info = models.TextField(blank=True, null=True)
    regionas = models.CharField(                         #galimybe rinktis regiona
        max_length=20,
        choices=[('Rinkis', 'Rinkis')] + list(REGIONAI),
        default='Rinkis',
    )
    vieta = models.CharField(max_length=100, blank=True, null=True)  # Pridedame lauką "vieta"

    def __str__(self):
        return self.pavadinimas


class Privalumas(models.Model):
    pavadinimas = models.CharField(max_length=50)
    stovyklaviete = models.ForeignKey(Stovyklaviete, on_delete=models.CASCADE)

    def __str__(self):
        return self.pavadinimas