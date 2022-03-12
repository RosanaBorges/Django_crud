from django.db import models

class Clientes(models.Model):
    Id = models.BigAutoField(primary_key=True)
    NomeCliente = models.CharField(max_length=150)
    CPF = models.CharField(max_length=11)
    Endereco = models.CharField(max_length=100)
    Celular = models.CharField(max_length=11)
    Email = models.EmailField(max_length=100)
