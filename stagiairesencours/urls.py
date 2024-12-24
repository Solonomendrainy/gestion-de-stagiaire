
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    
    path('',views.stagiairesencours_view, name='stagiairesencours'),
    path('edit/',views.Edit, name='edit'),
    path('update/<str:id>',views.UpdateEncrs, name='update'),
    path('delete/<str:id>',views.DeleteStagEncours, name='delete'),   
    path('send_email/<str:id>', views.send_email_to_stagiaire, name='send_email'),
    path('certificate/<int:id>/', views.view_certificate, name='view_certificate'),
     path('listeEncours/',views.ListeEncours, name='listeEncours'), 
]