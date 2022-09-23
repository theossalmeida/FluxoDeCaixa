from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Tipo(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Lancamento(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    usuario = models.CharField(max_length=50)
    data = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome