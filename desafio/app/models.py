from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.IntegerField()

    def __str__(self):
        return self.nome

class PostoAtendimento(models.Model):
    nome = models.CharField(Cliente, max_length=100)
    cpf = models.IntegerField(Cliente)
    combustivel = models.CharField(max_length=50)
    quantidade = models.FloatField()
    valorPago = models.FloatField()

    def __str__(self):
        return self.nome