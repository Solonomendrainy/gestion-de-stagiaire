from django.shortcuts import render , get_object_or_404, redirect
from django.http import HttpResponse

from encadrents.models import Encadrents
from stagiaires.models import Stagiaire
from stagiairesencours.models import Stagiairesencours
from stages.models import Stages
from sweetify import sweetify

def encadrant_view(request):
    emp = Encadrents.objects.all()
    if request.method == "GET":
        nom = request.GET.get('recherche')
        if nom is not None:
           emp = Encadrents.objects.filter(nom__icontains=nom)
           
    stg = Stagiaire.objects.all()
    Encours= Stagiairesencours.objects.all()
    stage  = Stages.objects.all()
    
     # Comptez le nombre de stagiaires
    nombre_stagiairesNouveaux = stg.count()
    # Comptez le nombre des encadrent
    nombre_encadrent = emp.count()
     # Comptez le nombre de stagiaires en cours
    nombre_stagiairesEncours = Encours.count()
    stage = stage.count()
    
    context = {
        'emp':emp,
        'nombre_stagiairesNouveaux': nombre_stagiairesNouveaux,  # Ajoutez ce nombre au contexte
        'nombre_encadrent': nombre_encadrent,  # Ajoutez ce nombre au contexte
        'nombre_stagiairesEncours': nombre_stagiairesEncours,  # Ajoutez ce nombre au contexte
        'stage':stage,
    }
    return render(request, 'encadrent.html',context)



def ADDencadrent (request):
    if request.method == "POST" :
        cin = request.POST.get('cin')
        nom = request.POST.get('nom')
        prenom =request.POST.get('prenom')
        email =request.POST.get('email')
        division =request.POST.get('division')
        phone =request.POST.get('phone')
        
        emp = Encadrents(
            cin = cin,
            nom = nom,
            prenom = prenom,
            email = email,
            phone = phone,
            division = division,
        )
        emp.save()
        sweetify.success(request, 'L encadreur a été ajouter avec succès', icon='success')
        return redirect('encadrents')
   
    return render(request, 'encadrent.html')

def Edit (request):
    emp = Encadrents.objects.all()
    
    context = {
        'emp':emp
        
    }
    return redirect(request, 'encadrent.html',context)

def Update (request, id) :
     if request.method == "POST" :
        cin = request.POST.get('cin')
        nom = request.POST.get('nom')
        prenom =request.POST.get('prenom')
        email =request.POST.get('email')
        division =request.POST.get('division')
        phone =request.POST.get('phone')
        
        emp = Encadrents(
            id = id ,
            cin = cin,
            nom = nom,
            prenom = prenom,
            email = email,
            phone = phone,
            
            division = division ,
           
        )
        emp.save()
        sweetify.success(request, 'L encadreur a été modifier avec succès', icon='success')
     return redirect('encadrents')
     return redirect(request, 'stagiaire.html')
 
 
def Delete(request,id):
     emp = Encadrents.objects.filter(id = id)
     emp.delete()
     context = {
         'emp':emp  
      }
     sweetify.success(request, 'L encadreur a été supprimer avec succès', icon='success')
     return redirect('encadrents')
 
def ListeEnc(request):
    emp = Encadrents.objects.all()
    context = {
        'emp':emp,
    }
    return render(request, 'encadrents.html',context) 
     

















