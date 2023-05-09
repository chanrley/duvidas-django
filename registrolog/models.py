from django.db import models

class LogRegistro(models.Model):
    """Objeto do tipo LogRegistro para gravar todos os passos do usuário dentro do sistema """
    campo = models.TextField()
    data_insercao = models.DateTimeField(auto_now=True)
    

