from django.db import models

class LogRegistro(models.Model):
    campo = models.TextField()
    data_insercao = models.DateTimeField(auto_now=True)
    

