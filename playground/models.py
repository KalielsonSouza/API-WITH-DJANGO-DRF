from django.db import models

class Person(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    nome = models.CharField(max_length=35)
    sobrenome = models.CharField(max_length=35,null=True)
    sexo = models.CharField(max_length=2)
    altura = models.IntegerField()
    peso = models.FloatField()
    nascimento = models.DateField()
    bairro = models.CharField(max_length=55)
    cidade = models.CharField(max_length=55)
    estado = models.CharField(max_length=55)
    numero = models.IntegerField()
    idade = models.IntegerField()
class xsls(models.Model):
    file_name = models.FileField(upload_to='xlsx')
    uploaded = models.DateField(auto_now=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"file id{self.id}"