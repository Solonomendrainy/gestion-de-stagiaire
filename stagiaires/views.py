from django.shortcuts import render , get_object_or_404, redirect
from django.http import HttpResponse

from stagiaires.models import Stagiaire
from encadrents.models import Encadrents
from stages.models import Stages
from stagiairesencours.models import Stagiairesencours
from sweetify import sweetify
from django.template.context_processors import request


def stagiaire_view(request):
    emp = Stagiaire.objects.all()
    if request.method == "GET":
        nom = request.GET.get('recherche')
        if nom is not None:
           emp = Stagiaire.objects.filter(nom__icontains=nom)
    
    stg = Encadrents.objects.all()
    star  = Stages.objects.all()
    stgencours  = Stagiairesencours.objects.all()
    
     # Comptez le nombre de stagiaires
    nombre_stagiairesNouveaux = emp.count()
    nombre_encadrent = stg.count()
    stage = star.count()
    nombre_stagiairesEncours = stgencours.count()
    
    context = {
        'star':star,
        'emp':emp,
        'stg':stg,
        'stage':stage,
        'stgencours':stgencours,
        'nombre_stagiairesNouveaux': nombre_stagiairesNouveaux,  # Ajoutez ce nombre au contexte
        'nombre_stagiairesEncours': nombre_stagiairesEncours,
        'nombre_encadrent': nombre_encadrent,  # Ajoutez ce nombre au contexte
    }
    return render(request, 'stagiaire.html',context)



def ADD (request):
    if request.method == "POST" :
        cin = request.POST.get('cin')
        nom = request.POST.get('nom')
        prenom =request.POST.get('prenom')
        email =request.POST.get('email')
        qualite =request.POST.get('qualite')
        etablissement =request.POST.get('etablissement')
        findustage =request.POST.get('findustage')
        phone =request.POST.get('phone')
        
        emp = Stagiaire(
            cin = cin,
            nom = nom,
            prenom = prenom,
            email = email,
            phone = phone,
            findustage = findustage,
            qualite = qualite ,
            etablissement = etablissement,
        )
        emp.save()
        sweetify.success(request, 'le stagiaire a ete ajoute avec succes', icon='success')
        return redirect('stagiaires')
   
    return render(request, 'stagiaire.html')

def Edit (request):
    emp = Stagiaire.objects.all()
    
    context = {
        'emp':emp
        
    }
    return redirect(request, 'stagiaire.html',context)

def Updatest (request, id) :
     if request.method == "POST" :
        cin = request.POST.get('cin')
        nom = request.POST.get('nom')
        prenom =request.POST.get('prenom')
        email =request.POST.get('email')
        qualite =request.POST.get('qualite')
        etablissement =request.POST.get('etablissement')
        findustage =request.POST.get('findustage')
        phone =request.POST.get('phone')
        
        try:
             emp = Stagiaire(
                 id = id ,
                 cin = cin,
                 nom = nom,
                  prenom = prenom,
                 email = email,
                 phone = phone,
                 findustage = findustage,
                 qualite = qualite ,
                 etablissement = etablissement,
               )
             emp.save()
             sweetify.success(request, 'le stagaire a ete modifie avec succes', icon='success')
        except Exception as e:
            # Fermer le SweetAlert en cas d'erreur
            sweetify.error(request,'Echec de l envoie', icon='error')
     return redirect('stagiaires')
     return redirect(request, 'stagiaire.html')
 
 
def Delete(request,id):
     emp = Stagiaire.objects.filter(id = id)
     emp.delete()
     context = {
         'emp':emp  
      }
     sweetify.success(request, 'le stagiaire a ete supprimer avec succes', icon='success')
     return redirect('stagiaires')
 
def AFF(request):
    if request.method == "POST":
        cin = request.POST.get('cin')
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        qualite = request.POST.get('qualite')
        etablissement = request.POST.get('etablissement')
        findustage = request.POST.get('findustage')
        phone = request.POST.get('phone')
        encadrent = request.POST.get('encadrent')
        division = request.POST.get('division')
        stage = request.POST.get('stage')
        debutdustage = request.POST.get('debutdustage')
        email = request.POST.get('email')

        # Sauvegarde du stagiaire dans Stagiairesencours
        stgencours = Stagiairesencours(
            cin=cin,
            nom=nom,
            prenom=prenom,
            email=email,
            phone=phone,
            findustage=findustage,
            qualite=qualite,
            etablissement=etablissement,
            encadrent=encadrent,
            division=division,
            stage=stage,
            debutdustage=debutdustage,
        )
        stgencours.save()

        # Suppression du stagiaire de la table Stagiaire
        Stagiaire.objects.filter(cin=cin).delete()

    # Redirection vers la vue qui affiche les stagiaires en cours
    return redirect('stagiairesencours')


def Liste(request):
    emp = Stagiaire.objects.all()
    context = {
        'emp':emp,
    }
    return render(request, 'stagiaire.html',context)
     

















