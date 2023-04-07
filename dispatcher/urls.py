"""traveler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views

urlpatterns = [
    path('authorisation/sign_up/', views.sign_up, name='sign_up'),
    path('authorisation/sign_in/', views.sign_in, name='sign_in'),
    path('authorisation/change_name/', views.change_name, name='change_name'),
    path('landmarks/get_landmark/', views.get_landmark, name='get_landmark'),
    path('landmarks/get_landmark/', views.suggest_landmark, name='suggest_landmark')
]