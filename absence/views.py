from django.shortcuts import render , get_object_or_404, redirect
from django.http import HttpResponse

from absence.models import Absence
from encadrents.models import Encadrents
from stagiaires.models import Stagiaire
from sweetify import sweetify

from stagiaires.models import Stagiaire
from stagiairesencours.models import Stagiairesencours
from stages.models import Stages

def absence_view(request):
    abs = Absence.objects.all().select_related('stagiaire')  # Récupère les absences avec les stagiaires associés
    emp = Stagiairesencours.objects.all()  # Récupère tous les stagiaires
    enc = Encadrents.objects.all()
    Nouv = Stagiaire.objects.all() 
    stage  = Stages.objects.all()
    
    # Comptez le nombre de stagiaires
    nombre_stagiairesEncours = emp.count()
     # Comptez le nombre des encadrent
    nombre_encadrent = enc.count()
    # Comptez le nombre de  nouveaux stagiaires
    nombre_stagiairesNouveaux = Nouv.count()
    stage = stage.count()
    
    
    context = {
        'abs': abs,
        'emp': emp , # Ajoute la liste des stagiaires au contexte
        'nombre_stagiairesEncours': nombre_stagiairesEncours,  # Ajoutez ce nombre au contexte
        'nombre_stagiairesNouveaux': nombre_stagiairesNouveaux,  # Ajoutez ce nombre au contexte
        'nombre_encadrent': nombre_encadrent,  # Ajoutez ce nombre au contexte
        'stage':stage,
    }
    return render(request, 'absence.html', context)

def ADDAbsence(request):
    emp = Stagiairesencours.objects.all()  # Récupère tous les stagiaires
    if request.method == "POST":
        cin = request.POST.get('cin')
        stagiaire = get_object_or_404(Stagiairesencours, cin=cin)

        abs = Absence(
            stagiaire=stagiaire,
            cin = request.POST.get('cin'),
            nom = request.POST.get('nom'),
            prenom =request.POST.get('prenom'),
            justification=request.POST.get('justification'),
            date_debut=request.POST.get('date_debut'),
            date_fin=request.POST.get('date_fin'),
        )
        abs.save()
        sweetify.success(request, 'L absence a été marque avec succès', icon='success')
        return redirect('absence')

    context = {
        'emp': emp,  # Ajoute la liste des stagiaires au contexte
    }
    return render(request, 'absence.html', context)

def Edit (request):
    emp = Absence.objects.all()
    
    context = {
        'emp':emp
        
    }
    return redirect(request, 'absence.html',context)

def Updateabsence (request, id) :
     if request.method == "POST" :
        cin = request.POST.get('cin')
        nom = request.POST.get('nom')
        prenom =request.POST.get('prenom')
        justification =request.POST.get('justification')
        date_debut =request.POST.get('date_debut')
        date_fin =request.POST.get('date_fin')
        
        abs = Absence(
            id = id ,
            cin = cin,
            nom = nom,
            prenom = prenom,
            justification = justification,
            date_debut = date_debut,
            date_fin = date_fin ,
        )
        abs.save()
        sweetify.success(request, 'L absence a été odifie avec succès', icon='success')
     return redirect('absence')
     return redirect(request, 'absence.html')
 
 
def Delete(request,id):
     abs = Absence.objects.filter(id = id)
     abs.delete()
     context = {
         'abs':abs  
      }
     sweetify.success(request, 'L absence a été supprimé avec succès', icon='success')
     return redirect('absence')
     

















