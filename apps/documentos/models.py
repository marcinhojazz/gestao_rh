from django.db import models
# importando App Funcionarios 
from apps.funcionarios.models import Funcionario

# Create your models here.
class Documento(models.Model):
    description = models.CharField(max_length=100)
    # adicionando a classe pertence importada pela app Funcionarios
    belong = models.ForeignKey(
        Funcionario,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.description
