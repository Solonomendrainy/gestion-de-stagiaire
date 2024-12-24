
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    
    path('',views.stagiaire_view, name='stagiaires'),
    path('add/',views.ADD, name='add'),
    path('edit/',views.Edit, name='edit'),
    path('updates/<str:id>',views.Updatest, name='updates'),
    path('deletestagiaires/<str:id>',views.Delete, name='deletestagiaires'),
     path('aff/',views.AFF, name='aff'),
      path('liste/',views.Liste, name='liste'), 
     
]