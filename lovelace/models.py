from django.db import models
from django.utils import timezone

# Create your models here.

class Usuario(models.Model):
    nome_usuario = models.CharField(max_length=100, verbose_name="Nome")
    dt_nasc_usuario = models.DateField(verbose_name="Data de Nascimento")
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
    telefone_parceiras = models.CharField(max_length=11)
    celular_parceiras = models.CharField(max_length=11)
    email_parceiras = models.EmailField(max_length=30)
    class Meta:
        verbose_name_plural = "Parceiras"

class Votacao(models.Model):
    votos = models.IntegerField(default=0)
    class Meta:
        verbose_name_plural = "Votacao"

class Opiniao(models.Model):
    opiniao = models.TextField()
    class Meta:
        verbose_name_plural = "Opiniao"