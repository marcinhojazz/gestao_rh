from django.db import models

# Create your models here.
class Empresa(models.Model):
    name = models.CharField(max_length=100, help_text="Nome da Empresa")
    