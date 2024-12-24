from django.db import models

class Stagiairesencours(models.Model):
    cin = models.IntegerField()
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.IntegerField()
    findustage = models.DateField()
    qualite = models.TextField()
    etablissement = models.TextField()
    stage = models.TextField()
    debutdustage = models.DateField()
    division = models.TextField()
    encadrent = models.TextField()
    def __str__(self):
        return self.nom
    
    from django.db import models

class Evaluation(models.Model):
    stagiaire = models.ForeignKey(Stagiairesencours, on_delete=models.CASCADE)
    critere = models.CharField(max_length=200)
    note = models.DecimalField(max_digits=5, decimal_places=2)
    commentaires = models.TextField(blank=True, null=True)
    date_evaluation = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Évaluation de {self.stagiaire.nom} - {self.critere}"

    