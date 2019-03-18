from django.shortcuts import render, redirect
from lovelace import forms
from .models import Usuario, Parceiras, Estabelecimento, Categoria, FiltroParceiras
# Incluir os modelos/classes (definidos em models.py)

# Create your views here.

def render_index(request):
    return render(request, 'index.html')

def render_cadastrousuario(request):
    form = forms.UsuarioCriarForm(request.POST or None)
    form.is_valid()
    return render(request, 'cadastrousuario.html', {'form': form})

def salvarusuario(request):
    form = forms.UsuarioCriarForm(request.POST or None)
    form.is_valid()
    usuario_obj = Usuario.objects.create()
    usuario_obj.nome_usuario = request.POST['nome_usuario']
    usuario_obj.dt_nasc_usuario = request.POST['dt_nasc_usuario']
    usuario_obj.email = request.POST['email']
    usuario_obj.senha = request.POST['senha']
    usuario_obj.save()
    return redirect('/cadastrousuario/')

def render_home(request):
    return render(request, 'home.html')

def render_maps(request):
    form = forms.Vota(request.POST or None)
    form.is_valid()

    return render(request, 'maps.html', {'form': form})

def render_guia(request):
    return render(request, 'guia.html')

def render_guiaresultados(request):
    estabelecimentos = Categoria.objects.all()
    return render(request, 'guiaresultados.html', {'items' : estabelecimentos})

def render_guiaresultadosbalada(request):
    estabelecimentos = Categoria.objects.all()
    return render(request, 'guiaresultadosbalada.html', {'items' : estabelecimentos})

def render_guiaresultadosacademia(request):
    estabelecimentos = Categoria.objects.all()
    return render(request, 'guiaresultadosacademia.html', {'items' : estabelecimentos})

def render_guiaresultadosparque(request):
    estabelecimentos = Categoria.objects.all()
    return render(request, 'guiaresultadosparque.html', {'items' : estabelecimentos})

def render_guiaresultadoslazer(request):
    estabelecimentos = Categoria.objects.all()
    return render(request, 'guiaresultadoslazer.html', {'items' : estabelecimentos})

def render_guiaresultadosoutros(request):
    estabelecimentos = Categoria.objects.all()
    return render(request, 'guiaresultadosoutros.html', {'items' : estabelecimentos})

def render_parceiras(request):
    return render(request, 'parceiras.html')
 
def render_parceirasresultados(request):
    parceiras = FiltroParceiras.objects.all()
    return render(request, 'parceirasresultados.html', {'itemsparceiras' : parceiras})

def render_cadastroparceiras(request):
    form = forms.ParceirasCriarForm(request.POST or None)
    form.is_valid()
    return render(request, 'cadastroparceiras.html', {'form': form})

def salvarparceiras(request):
    form = forms.ParceirasCriarForm(request.POST or None)
    form.is_valid()
    parceira_obj = Parceiras.objects.create()
    parceira_obj.nome_parceira = request.POST['nome_parceira']
    parceira_obj.formacao = request.POST['formacao']
    parceira_obj.profissao = request.POST['profissao']
    parceira_obj.endereco_atend = request.POST['endereco_atend']
    parceira_obj.tipo_atend = request.POST['tipo_atend']
    parceira_obj.valor = request.POST['valor']
    parceira_obj.telefone_parceiras = request.POST['telefone_parceiras']
    parceira_obj.celular_parceiras = request.POST['celular_parceiras']
    parceira_obj.email_parceiras = request.POST['email_parceiras']
    parceira_obj.save()

    return redirect('/cadastroparceiras/')

def render_forum(request):
    return render(request, 'forum.html')