from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls'), name='login'),
    path('home/', views.home_view, name='home'),
    path('articles/', views.article_view, name='articles'),
    path('listesdessatgiaires/', views.listesdesstagiaires_view, name='listesdessatgiaires'),
    
    path('stagiaire/',include('stagiaires.urls'), name='stagiaires'),
     path('stagiairesencours/',include('stagiairesencours.urls'), name='stagiairesencour'),
    path('absence/',include('absence.urls'), name='absence'),
    path('stage/',include('stages.urls'), name='stages'),  
    path('encadrent/',include('encadrents.urls'), name='encadrents'),
    
     # urls pour le lgin page et inscription.
    path('login/',include('login.urls')), 
   
]
