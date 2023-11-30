from django.db import models

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    id_estampadores = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'