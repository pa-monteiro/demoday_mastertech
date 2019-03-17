from django.shortcuts import render
from lovelace import forms
# Incluir os modelos/classes (definidos em models.py)


# Create your views here.

def render_index(request):
    return render(request, 'index.html')

def render_cadastrousuario(request):
    form = forms.UsuarioCriarForm(request.POST or None)

    form.is_valid()

    return render(request, 'cadastrousuario.html', {'form': form})

def render_home(request):
    return render(request, 'home.html')

def render_maps(request):
    form = forms.Vota(request.POST or None)
    form.is_valid()

    return render(request, 'maps.html', {'form': form})

def render_guia(request):
    return render(request, 'guia.html')

def render_guiaresultados(request):
    return render(request, 'guiaresultados.html')

def render_guiaresultadosdetalhe(request):
    return render(request, 'guiaresultadosdetalhe.html')

def render_parceiras(request):
    return render(request, 'parceiras.html')
 
def render_parceirasresultados(request):
    return render(request, 'parceirasresultados.html')

def render_cadastroparceiras(request):
    form = forms.ParceirasCriarForm(request.POST or None)
    form.is_valid()

    return render(request, 'cadastroparceiras.html', {'form': form})

def render_forum(request):
    return render(request, 'forum.html')