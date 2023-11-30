from django.db import models
from django.utils import timezone

from django.contrib.auth import get_user_model

User = get_user_model()

class Status(models.Model):

    def __str__(self):
        return self.nome

    nome = models.CharField(max_length=100)
    dataHoraCriacao = models.DateTimeField(default=timezone.now)

class Aparelho(models.Model):
    def __str__(self):
        return self.marca + " - " + self.modelo + " - " + str(self.status)
    
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    dataHoraCriacao = models.DateTimeField(default=timezone.now)

class Emprestimo(models.Model):
    def __str__(self):
        return self.user.get_username() + ' solicitou o emprestimo da maquina ' + self.aparelho.marca + ' ' + self.aparelho.modelo + ' - situação: ' + self.aparelho.status.nome

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    aparelho = models.ForeignKey(Aparelho, related_name='aparelhos', on_delete=models.CASCADE)
    dataEmprestimo = models.DateTimeField(default=timezone.now)
    dataDevolucao = models.DateTimeField(default=timezone.now)

