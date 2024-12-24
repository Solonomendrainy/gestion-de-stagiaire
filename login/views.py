from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
import json
from django.shortcuts import render
from encadrents.models import Encadrents
from stagiaires.models import Stagiaire
from stages.models import Stages
from stagiairesencours.models import Stagiairesencours
@login_required(login_url='login')

@login_required(login_url='login')
def HomePage(request):
    # Récupération des objets
    emp = Stages.objects.all()
    enc = Encadrents.objects.all()
    stg = Stagiaire.objects.all()
    Encours = Stagiairesencours.objects.all()

    # Comptage des éléments
    nombre_stagiairesNouveaux = stg.count()
    nombre_encadrent = enc.count()
    nombre_stagiairesEncours = Encours.count()
    stage = emp.count()

    # Préparer les données à envoyer dans le contexte
    context = {
        'emp': emp,
        'nombre_stagiairesNouveaux': nombre_stagiairesNouveaux,
        'nombre_encadrent': nombre_encadrent,
        'stagiaires_en_cours': nombre_stagiairesEncours,
        'stages': stage,
        # Convertir les QuerySets en dictionnaires sérialisables
        'data': json.dumps({
            'stagiaires': {
                'nouveaux': nombre_stagiairesNouveaux,
                'en_cours': nombre_stagiairesEncours,
                'nombre_encadrent': nombre_encadrent,
                'stages': stage
            }
        })
    }

    return render(request, 'home.html', context)

def SignupPage_view(request):
    if request.method == 'POST':
        if 'nom' in request.POST:
            # Traitement du formulaire d'inscription
            username = request.POST.get('nom')
            email = request.POST.get('email')
            password1 = request.POST.get('motdepasse1')
            password2 = request.POST.get('motdepasse2')

            if password1 != password2:
                messages.error(request, "Les mots de passe ne correspondent pas")
            elif not username or not email or not password1:
                messages.error(request, "Veuillez remplir tous les champs")
            else:
                try:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    user.save()
                    # Authentifier et connecter l'utilisateur après l'inscription
                    user = authenticate(username=username, password=password1)
                    if user is not None:
                        login(request, user)
                        messages.success(request, "Compte créé et connexion réussie")
                        return redirect('home')
                except Exception as e:
                    messages.error(request, f"Une erreur s'est produite : {str(e)}")

        else:
            # Traitement du formulaire de connexion
            username = request.POST.get('username')
            password = request.POST.get('password')

            if not username or not password:
                messages.error(request, "Veuillez remplir tous les champs")
            else:
                user = authenticate(username=username, password=password)
                
                if user is not None:
                    login(request, user)
                    messages.success(request, "Connexion réussie")
                    return redirect('home')
                else:
                    messages.error(request, "Nom d'utilisateur ou mot de passe incorrect")

    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


def list_users(request):
    users = User.objects.all()  # Récupérer tous les utilisateurs
    context = {
        'users': users
    }
    return render(request, 'compte.html',context)

@login_required(login_url='login')
def add_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Vérifications des mots de passe
        if password1 != password2:
            messages.error(request, "Les mots de passe ne correspondent pas.")
        else:
            # Création de l'utilisateur
            try:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, "L'utilisateur a été créé avec succès.")
                return redirect('list_users')  # Rediriger vers la liste des utilisateurs
            except Exception as e:
                messages.error(request, f"Une erreur s'est produite lors de la création de l'utilisateur : {e}")

    return render(request, 'compte.html')


@login_required(login_url='login')
def delete_user(request,user_id):
     emp = User.objects.filter(id = user_id)
     emp.delete()
     context = {
         'emp':emp  
      }
     return redirect('list_users')