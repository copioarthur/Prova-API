from django.db import models

class Genero(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    descricao = models.TextField(blank=True)

def __str__(self):
    return self.nome
    
class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    sinopse = models.TextField(blank=True)
    ano_lancamento = models.IntegerField(default=0)
    nota = models.DecimalField(max_length=10, decimal_places=2, max_digits=4)
    disponivel = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    genero = models.ForeignKey(
        'Genero',
        on_delete=models.SET_NULL,
        null=True,
        related_name='filmes'
)

def __str__(self):
    return self.titulo