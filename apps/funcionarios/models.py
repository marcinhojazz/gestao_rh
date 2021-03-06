from django.db import models
from django.contrib.auth.models import User #importando modulo AUTH User
# importando app departamentos
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa
from django.urls import reverse

# Create your models here.a
class Funcionario(models.Model):
    name = models.CharField(max_length=100)
    username = models.OneToOneField(User, on_delete=models.PROTECT, unique=True)
    # adicionando a classe departamentos que foi importada apartir de apps.
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('list_funcionarios')

    def __str__(self):
        return self.name