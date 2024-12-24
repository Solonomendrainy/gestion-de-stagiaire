from django.shortcuts import render , get_object_or_404, redirect
from django.http import HttpResponse
from .db_articles import articles

from stagiaires.models import Stagiaire

def home_view(request):
    emp = Stagiaire.objects.all()
    nombre_stagiaires = emp.count()
    
    context = {
        'emp':emp,
        'nombre_stagiaires': nombre_stagiaires,
        # Ajoutez d'autres éléments de contexte si nécessaire
        }
    return render(request, 'home.html', context)


def article_view(request):
    return render(request, 'articles.html' , context={'articles' : articles})

def listesdesstagiaires_view(request):
    return render(request, 'dashbord.html')


     









