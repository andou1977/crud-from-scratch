from django.db import models

# Create your models here.

class Sogebank(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    solde = models.IntegerField()
    email = models.CharField(max_length=50)
    date = models.DateField()
    active = models.BooleanField()

    class Meta:
        ordering = ('nom',)

    def __str__(self):
        return self.nom
