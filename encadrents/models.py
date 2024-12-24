from django.db import models
class Encadrents(models.Model):
    cin = models.IntegerField()
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.IntegerField()
    division = models.TextField()
    def __str__(self):
        return self.nom
    