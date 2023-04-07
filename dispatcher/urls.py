from django.urls import path

from . import views

urlpatterns = [
    path('authorisation/sign_up/', views.sign_up, name='sign_up'),
    path('authorisation/sign_in/', views.sign_in, name='sign_in'),
    path('authorisation/change_name/', views.change_name, name='change_name'),
    path('landmarks/get_landmark/', views.get_landmark, name='get_landmark'),
    path('landmarks/suggest_landmark/', views.suggest_landmark, name='suggest_landmark')
]