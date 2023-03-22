from django.test import TestCase

from django.db import models
from .models import LogRegistro

f = open("zdemofile.txt", "r")
for x in f:
#   print(x)
    registro = LogRegistro(campo=x)
print(registro)
