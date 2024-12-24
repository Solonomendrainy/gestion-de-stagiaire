from django.contrib import admin
from django.urls import path
from . import views
from .views import  SignupPage_view, HomePage , LogoutPage
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', SignupPage_view, name='login'),
    path('home/', HomePage, name='home'),
    path('logout/', LogoutPage, name='logout'), 
    
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('list_users/', views.list_users, name='list_users'),
    path('add_user/', views.add_user, name='add_user'),
     path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    
]  

