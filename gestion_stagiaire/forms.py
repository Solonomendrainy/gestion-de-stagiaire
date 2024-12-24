from django import forms
from .models import Stagiaire

class StagiaireForm(forms.ModelForm):
    class Meta:
        model = Stagiaire
        fields = ['nom', 'prenom', 'email', 'date_naissance', 'stage_en_cours']
