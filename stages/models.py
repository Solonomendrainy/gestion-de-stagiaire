from django.db import models

class Stages(models.Model):
    titre = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return self.titre
