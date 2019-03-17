"""demoday_projeto URL Configuration
 
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from lovelace import views
from django.views.generic import TemplateView
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.render_index),
    path('cadastrousuario/', views.render_cadastrousuario),
    path('home/', views.render_home),
    path('maps/', views.render_maps),
    path('guia/', views.render_guia),
    path('guiaresultados/', views.render_guiaresultados),
    path('parceiras/', views.render_parceiras),
    path('parceirasresultados/', views.render_parceirasresultados),
    path('cadastroparceiras/', views.render_cadastroparceiras),
    path('forum/', views.render_forum),
    path('salvarparceiras/', views.salvarparceiras)
]