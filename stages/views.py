from django.shortcuts import render , get_object_or_404, redirect
from django.http import HttpResponse

from encadrents.models import Encadrents
from stagiaires.models import Stagiaire
from stages.models import Stages
from stagiairesencours.models import Stagiairesencours
from sweetify import sweetify

def stage_view(request):
    emp = Stages.objects.all()
    enc = Encadrents.objects.all()
    stg = Stagiaire.objects.all()
    Encours= Stagiairesencours.objects.all()
    
     # Comptez le nombre de nouveaux stagiaires
    nombre_stagiairesNouveaux = stg.count()
    # Comptez le nombre des encadrent
    nombre_encadrent = enc.count()
     # Comptez le nombre de stagiaires en cours
    nombre_stagiairesEncours = Encours.count()
     # Comptez le nombre de stage
    stage = emp.count()
    
    context = {
        'emp':emp,
        'nombre_stagiairesNouveaux': nombre_stagiairesNouveaux,  # Ajoutez ce nombre au contexte
        'nombre_encadrent': nombre_encadrent,  # Ajoutez ce nombre au contexte
        'nombre_stagiairesEncours': nombre_stagiairesEncours,  # Ajoutez ce nombre au contexte
         'stage': stage,  # Ajoutez ce nombre au contexte
    }
    return render(request, 'stage.html',context)



def ADD(request):
    if request.method == "POST" :
        titre = request.POST.get('titre')
        date_debut=request.POST.get('date_debut')
        date_fin=request.POST.get('date_fin')
        
        emp = Stages(
            titre = titre,
            date_debut = date_debut,
            date_fin = date_fin,
        )
        sweetify.success(request, 'Le stage a été ajouter avec succès', icon='success')
        emp.save()
        return redirect('stages')
   
    return render(request, 'stages.html')

def Edit (request):
    emp = Stages.objects.all()
    
    context = {
        'emp':emp
        
    }
    return redirect(request, 'stage.html',context)

def UpdateStages (request, id) :
     if request.method == "POST" :
        titre = request.POST.get('titre')
        date_debut =request.POST.get('date_debut')
        date_fin =request.POST.get('date_fin')
        
        emp = Stages(
            id = id ,
            titre = titre,
            date_debut = date_debut,
            date_fin = date_fin,
        )
        emp.save()
        sweetify.success(request, 'Le stage a été modifier avec succès', icon='success')
     return redirect('stages')
     return redirect(request, 'stage.html')
 
 
def Delete(request,id):
     emp = Stages.objects.filter(id = id)
     emp.delete()
     context = {
         'emp':emp  
      }
     sweetify.success(request, 'Le stage a été supprimé avec succès', icon='success')
     return redirect('stages')
     

















