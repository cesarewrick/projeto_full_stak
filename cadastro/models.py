from django.db import models

# Create your models here.
class Estudante(models.Model):
    nome = models.CharField(max_length=100, null=False, blanck=False)
    cpf = models.CharField(max_length=11, null=False, blank=False, primary_key=True)
    email = models.EmailField(max_length=100, null=False, blank=False)
    endereco = models.CharField(max_length=100,)
    telefone = models.CharField(max_length=14, null=False, blanck=False)
    data_nacimento = models.DateField()

    def __str__(self):
        return self.nome

class Curso(models.Model):
    NIVEL = (
        ('B', "Basico"),
        ('I', "Intermediario"),
        ('A', "Avançado"),
    )
    codigo = models.CharField(max_length=14, blanck=False)
    descricao = models.CharField(max_length=100, null=False, blanck=False)
    nivel = models.CharField(max_length=1, choices = NIVEL, null=False, blanck=False, default= 'B')



    def __str__(self):
        return self.codigo