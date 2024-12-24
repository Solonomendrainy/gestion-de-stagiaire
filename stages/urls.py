
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    
    path('',views.stage_view, name='stages'),
     path('addStages/',views.ADD, name='addStages'),
     path('edit/',views.Edit, name='edit'),
     path('updateSitage/<str:id>',views.UpdateStages, name='updateSitage'),
     path('deleteStages/<str:id>',views.Delete, name='deleteStages'),

     
]