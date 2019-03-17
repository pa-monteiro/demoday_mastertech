from django.urls import path
from . import views
#Aqui estmaos importando do Django a função url e todas as nossas views do aplicativo

urlpatterns = [
    path('/index/', views.index, name="index"),
    # atribui a view chamada index para a URL raiz
    # name="index" é o nome da URL que será usado apra identificar a view
    path('/maps/', views.maps, name="maps"),
    path('/cadastrousuario/', views.cadastrousuario, name="cadastrousuario"),
    path('/home/', views.home, name="home"),
    path('/guia/', views.guia, name="guia"),
    path('/guiaresultados/', views.guiaresultados, name="guiaresultados"),
    path('/parceiras/', views.parceiras, name="parceiras"),
    path('/parceirasresultados/', views.parceirasresultados, name="parceirasresultados"),
    path('/cadastroparceiras/', views.cadastroparceiras, name="cadastroparceiras"),
    path('/forum/', views.forum, name="forum")
]