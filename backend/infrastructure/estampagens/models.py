from django.db import models

class Estoque(models.Model):
    tipo = models.CharField(max_length=50, null=False)
    quantidade = models.IntegerField(null=False)

    def __str__(self) -> str:
        return self.tipo

class Estampagens(models.Model):
    ae = models.IntegerField()
    iniciado = models.DateField(auto_now=False)
    concluido = models.DateField(auto_now=False)
    tipo = models.ForeignKey(Estoque, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return "Estampagem de: " + self.tipo