from django.db import models
from stagiaires.models import Stagiaire
from stagiairesencours.models import Stagiairesencours

class Absence(models.Model):
    stagiaire = models.ForeignKey(Stagiairesencours, null=True, on_delete=models.SET_NULL)
    cin = models.IntegerField()
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    justification = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return self.nom
