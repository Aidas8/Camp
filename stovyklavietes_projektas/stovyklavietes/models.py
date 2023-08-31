from django.db import models

class Stovyklaviete(models.Model):
    pavadinimas = models.CharField(max_length=100)
    reitingas = models.PositiveIntegerField()
    koordinates = models.CharField(max_length=50, blank=True, null=True)   # Pridetas koordinaciu laukas
    nuotrauka = models.ImageField(upload_to='stovyklavietes/', blank=True, null=True)             # Pridetas nuotrauku laukas
    papildoma_info = models.TextField(blank=True, null=True)                                    # Pridetas papildoma_info laukas
    def __str__(self):
        return self.pavadinimas

class Privalumas(models.Model):
    pavadinimas = models.CharField(max_length=50)
    stovyklaviete = models.ForeignKey(Stovyklaviete, on_delete=models.CASCADE)

    def __str__(self):
        return self.pavadinimas