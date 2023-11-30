from django.db import models

ESTAMPAGENS_STATUSES = [
        ('CRIADO', 'Criado'),
        ('INICIADO', 'Iniciado'),
        ('EM_ESTAMPAGEM', 'Em_Estampagem'),
        ('CONCLUIDO', 'Concluido'),
        ('CANCELADO', 'Cancelado'),
    ]

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
    status = models.CharField(max_length=20, default="OPEN", choices=ESTAMPAGENS_STATUSES)

    def __str__(self) -> str:
        return "Estampagem de: " + self.tipo