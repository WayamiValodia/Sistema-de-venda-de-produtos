from django.db import models
from django.contrib.auth.models import User

class Productos(models.Model):
  nome = models.CharField(max_length=200)
  categoria = models.CharField(max_length=200)
  descricao = models.TextField(blank=True)
  lancamento = models.DateTimeField(auto_now_add=True)
  expiracao = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.nome+'-por:'+self.user.username