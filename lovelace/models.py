from django.db import models
from django.utils import timezone


# Create your models here.

class Usuario(models.Model):
    nome_usuario = models.CharField(max_length=100, verbose_name="Nome")
    dt_nasc_usuario = models.DateTimeField(verbose_name="Data de Nascimento", default="DD/MM/AAAA")
    email_usuario = models.EmailField(max_length=256, verbose_name="Email")
    senha_usuario = models.CharField(max_length=256, verbose_name="Senha")
    class Meta:
        verbose_name_plural = "Usuario"

class Parceiras(models.Model):
    nome_parceira = models.TextField()
    formacao = models.CharField(max_length=60)
    profissao = models.CharField(max_length=60)
    endereco_atend = models.CharField(max_length=100)
    tipo_atend = models.CharField(max_length=30)
    valor = models.CharField(max_length=10)
    telefone_parceiras = models.CharField(max_length=20)
    celular_parceiras = models.CharField(max_length=20)
    email_parceiras = models.EmailField(max_length=30)
    class Meta:
        verbose_name_plural = "Parceiras"

    def __str__(self):
        return self.nome_parceira

class FiltroParceiras(models.Model):
    #filtrar por profissão, advogada, personal, psicóloga
    parceiras = models.ForeignKey(Parceiras, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200, default='')
    class Meta:
        verbose_name_plural = "FiltroParceiras"

class Votacao(models.Model):
    votos = models.IntegerField(default=0)
    class Meta:
        verbose_name_plural = "Votacao"

class Opiniao(models.Model):
    opiniao = models.TextField()
    class Meta:
        verbose_name_plural = "Opiniao"

class TipoAtendimento(models.Model):
    def __str__(self):
        return self.opiniao

    tipoatendimento = models.IntegerField(default=0)

class Estabelecimento(models.Model):
    nome_estabelecimento = models.CharField(max_length=200)
    endereco_estabelecimento = models.CharField(max_length=200)
    horario_estabelecimento = models.CharField(max_length=200)
    telefone_estabelecimento = models.CharField(max_length=20, default='')
    class Meta:
        verbose_name_plural = "Estabelecimento"

    def __str__(self):
        return self.nome_estabelecimento

class Categoria(models.Model):
    estabelecimentos = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200, default='')
    class Meta:
        verbose_name_plural = "Categoria"