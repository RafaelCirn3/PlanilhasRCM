from django.db import models
from django.contrib.auth.models import User

class Servico(models.Model):
    nome = models.CharField(max_length=255)
    unidade_medida = models.CharField(max_length=50)
    escopo_minimo = models.FloatField()
    
    def __str__(self):
        return self.nome

class RegistroServico(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    local_execucao = models.CharField(max_length=255)
    executado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    realizado_periodo = models.FloatField()
    fotos = models.ImageField(upload_to='fotos_servicos/', blank=True, null=True)
    descricao = models.TextField()
    observacoes = models.TextField(blank=True, null=True)

    def percentual_realizado(self):
        return (self.realizado_periodo / self.servico.escopo_minimo) * 100
class HistoricoUsuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    acao = models.CharField(max_length=255)
    data = models.DateTimeField(auto_now_add=True)
