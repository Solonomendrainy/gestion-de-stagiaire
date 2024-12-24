
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    
    path('',views.encadrant_view, name='encadrents'),
    path('addencadrant/',views.ADDencadrent, name='addencadrant'),
    path('edit/',views.Edit, name='edit'),
    path('updateencadrent/<str:id>',views.Update, name='updateencadrent'),
    path('deleteencadrent/<str:id>',views.Delete, name='deleteencadrent'),
     path('listeEnca/',views.ListeEnc, name='listeEnca'), 
     
]