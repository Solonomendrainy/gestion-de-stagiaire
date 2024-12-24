from django.shortcuts import render , get_object_or_404, redirect
from django.http import HttpResponse

from stagiairesencours.models import Stagiairesencours, Evaluation
from encadrents.models import Encadrents
from stagiaires.models import Stagiaire
from django.core.mail import send_mail
from django.contrib import messages
from sweetify import sweetify
import json
from django.http import JsonResponse
from stages.models import Stages
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from django.shortcuts import get_object_or_404
from django.conf import settings
import os
from reportlab.lib.colors import HexColor



def stagiairesencours_view(request):
    encours = Stagiairesencours.objects.all()
    if request.method == "GET":
        nom = request.GET.get('recherche')
        if nom is not None:
           encours = Stagiairesencours.objects.filter(nom__icontains=nom)
           
    enc = Encadrents.objects.all()
    stg  = Stages.objects.all()
    Nouv = Stagiaire.objects.all()
     # Comptez le nombre de stagiaires
    nombre_stagiairesEncours = encours.count()
    nombre_encadrent = enc.count()
    stage = stg.count()
    nombre_stagiairesNouveaux = Nouv.count()
    
    context = {
        'encours':encours,
        'nombre_stagiairesNouveaux': nombre_stagiairesNouveaux,  # Ajoutez ce nombre au contexte
        'nombre_stagiairesEncours': nombre_stagiairesEncours,  # Ajoutez ce nombre au contexte
        'nombre_encadrent': nombre_encadrent,  # Ajoutez ce nombre au contexte
        'stage': stage,  # Ajoutez ce nombre au contexte
    }
    return render(request, 'stagiairesencours.html',context)

def Edit (request):
    encours = Stagiairesencours.objects.all()
    context = {
        'encours':encours
        
    }
    return redirect(request, 'stagiairesencours.html',context)

def UpdateEncrs (request, id) :
     if request.method == "POST" :
        cin = request.POST.get('cin')
        nom = request.POST.get('nom')
        prenom =request.POST.get('prenom')
        email =request.POST.get('email')
        qualite =request.POST.get('qualite')
        stage =request.POST.get('stage')
        etablissement =request.POST.get('etablissement')
        findustage =request.POST.get('findustage')
        debutdustage =request.POST.get('debutdustage')
        phone =request.POST.get('phone')
        encadrent =request.POST.get('encadrent')
        division =request.POST.get('division')
        
        encours = Stagiairesencours(
            id = id ,
            cin = cin,
            nom = nom,
            prenom = prenom,
            email = email,
            phone = phone,
            findustage = findustage,
            debutdustage = debutdustage,
            qualite = qualite ,
            stage = stage ,
            etablissement = etablissement,
            encadrent = encadrent,
            division= division,
        )
        encours.save()
        sweetify.success(request, 'Le stagiaire a été modifier avec succès', icon='success')
     return redirect('stagiairesencours')
     return redirect(request, 'stagiairesencours.html')
 
def DeleteStagEncours(request,id):
     encours = Stagiairesencours.objects.filter(id = id)
     encours.delete()
     context = {
         'encours':encours  
      }
     sweetify.success(request, 'Le stagiaire a été supprimé avec succès', icon='success')
     return redirect('stagiairesencours')
 
 
def send_email_to_stagiaire(request, id):
    # Récupère le stagiaire par son ID
    encours = get_object_or_404(Stagiairesencours, id=id)
    
    # Vérifie si la méthode est POST
    if request.method == "POST":
        subject = request.POST.get('subject')  # Objet de l'email
        message = request.POST.get('message')  # Message de l'email
        from_email ='solonomendrainy@gmail.com'  # Remplacez par votre email d'expéditeur
        
        try:
            send_mail(
                subject,
                message,
                from_email,
                [encours.email],  # L'email du stagiaire récupéré à partir du modèle
                fail_silently=False,
            )
            
            sweetify.success(request, 'Email envoyé avec succès', icon='success')
            messages.success(request, "L'email a été envoyé avec succès!")
        except Exception as e:
            # Fermer le SweetAlert en cas d'erreur
            sweetify.error(request,'Echec de l envoie', icon='error')
        
        return redirect('stagiairesencours')
    
    
# Fonction pour couper et ajuster le texte dans le PDF
def draw_text(canvas, text, x, y, max_width, font_name="Helvetica", font_size=12):
    canvas.setFont(font_name, font_size)
    lines = []
    words = text.split(" ")
    line = ""
    
    for word in words:
        # Tester si le mot ajoute à la ligne dépasse la largeur max
        test_line = line + " " + word if line else word
        width = canvas.stringWidth(test_line, font_name, font_size)
        
        if width <= max_width:
            line = test_line
        else:
            lines.append(line)
            line = word
    
    if line:  # Ajouter la dernière ligne
        lines.append(line)
    
    # Dessiner chaque ligne sur le PDF
    for line in lines:
        canvas.drawString(x, y, line)
        y -= font_size  # Espacer les lignes

    return y  # Retourner la nouvelle position verticale (après avoir écrit le texte)
    

def view_certificate(request, id):
    if request.method == "POST":
        # Récupérer les données du formulaire soumis
        critere = request.POST.get('critere')
        date_evaluation = request.POST.get('date_evaluation')
        note = request.POST.get('note')
        commentaire = request.POST.get('commentaire')

        # Récupérer le stagiaire par son ID
        stagiaire = get_object_or_404(Stagiairesencours, id=id)

        # Configurer la réponse pour un fichier PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="certificat_{stagiaire.nom}_{stagiaire.prenom}.pdf"'

        # Initialiser le PDF avec ReportLab
        p = canvas.Canvas(response, pagesize=letter)

        # Ajouter une image (logo ou autre)
        image_path = os.path.join(settings.BASE_DIR, 'static', 'image', 'logos.png')  # Chemin vers l'image
        if os.path.exists(image_path):
            p.drawImage(image_path, 400, 720, width=100, height=50)  # Position x, y et dimensions de l'image
         # Ajouter un espace entre l'image et le texte (ajuster la position y)
         
        y_position = 680  # Nouvelle position après l'image
        
        # Ajouter le contenu du certificat
        p.setFont("Helvetica-Bold", 18)
        p.setFillColor(HexColor('#2E8B57'))  # Couleur verte
        p.setFont("Helvetica-Bold", 18)
        p.drawString(100, 750, "CERTIFICAT DE FIN DE STAGE")

        y_position = 660
        p.setFont("Helvetica", 12)
        p.setFillColor(HexColor('#000000'))  # Couleur noire pour le texte principal
        # Utilisation de la fonction pour gérer l'ajustement du texte
        y_position = draw_text(p, f"Nom : {stagiaire.nom} {stagiaire.prenom} de CIN : {stagiaire.cin} d'établissement {stagiaire.etablissement} et il a la qualité {stagiaire.qualite}", 100, y_position, 400)
        y_position = draw_text(p, f"Et il a fait un stage chez nous à MADABRAIN le {stagiaire.debutdustage.strftime('%d/%m/%Y')} et termine le {stagiaire.findustage.strftime('%d/%m/%Y')}", 100, y_position, 400)
        y_position = draw_text(p, f"Et il est encadré par {stagiaire.encadrent} et il a occupé la place dans le stage {stagiaire.stage}", 100, y_position, 400)

        # Ajouter l'évaluation
       # Ajouter l'évaluation
        p.setFont("Helvetica-Bold", 14)
        p.setFillColor(HexColor('#4169E1'))  # Couleur bleue pour l'évaluation
        y_position = draw_text(p, f"                      .                        ", 100, y_position, 400)
        y_position = draw_text(p, "Évaluation :", 100, y_position, 400)
        
        p.setFont("Helvetica", 12)
        p.setFillColor(HexColor('#000000'))  # Couleur noire pour les détails
        y_position = draw_text(p, f"Critère : {critere}", 100, y_position, 400)
        y_position = draw_text(p, f"Date d'évaluation : {date_evaluation}", 100, y_position, 400)
        y_position = draw_text(p, f"Commentaire  : {commentaire}", 100, y_position, 400)
        y_position = draw_text(p, f"Note : {note}", 100, y_position, 400)

        # Ajouter la date de création
        p.setFont("Helvetica-Oblique", 10)
        y_position = draw_text(p, "Fait à l'établissement, ce jour.", 100, y_position, 400)
        
        y_position = 460
        y_position = draw_text(p, "siggnature", 400, y_position, 900)

        # Finaliser le PDF
        p.showPage()
        p.save()

        return response
    return redirect('stagiairesencours')

def add_evaluation(request, id):
    stagiaire = get_object_or_404(Stagiairesencours, id=id)

    if request.method == "POST":
        critere = request.POST.get('critere')
        date_evaluation = request.POST.get('date_evaluation')
        note = request.POST.get('note')
        commentaire = request.POST.get('commentaire')

        # Créer l'objet Evaluation
        evaluation = Evaluation(
            stagiaire=stagiaire,
            critere=critere,
            date_evaluation=date_evaluation,
            note=note,
            commentaire=commentaire,
        )
        evaluation.save()
        sweetify.success(request, 'Évaluation ajoutée avec succès!', icon='success')

    return redirect('stagiairesencours')  # Rediriger après l'ajout

def ListeEncours(request):
    encours = Stagiairesencours.objects.all()
    context = {
        'encours':encours,
    }
    return render(request, 'stagiairesencours.html',context)

