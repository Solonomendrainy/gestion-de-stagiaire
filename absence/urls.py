
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    
    path('',views.absence_view, name='absence'),
    path('addabsence/', views.ADDAbsence, name='addabsence'),
    path('edit/',views.Edit, name='edit'),
    path('updateabsence/<str:id>',views.Updateabsence, name='updateabsence'),
    path('deleteabsence/<str:id>',views.Delete, name='deleteabsence'),
     
]