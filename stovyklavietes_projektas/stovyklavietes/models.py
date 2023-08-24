from django.db import models

class Stovyklaviete(models.Model):
    pavadinimas = models.CharField(max_length=100)
    reitingas = models.PositiveIntegerField()

    def __str__(self):
        return self.pavadinimas

class Privalumas(models.Model):
    pavadinimas = models.CharField(max_length=50)
    stovyklaviete = models.ForeignKey(Stovyklaviete, on_delete=models.CASCADE)

    def __str__(self):
        return self.pavadinimas