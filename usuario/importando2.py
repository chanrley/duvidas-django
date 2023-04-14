import csv, sys, os, django


project_dir = "/novo_portal_DVA/usuario/"
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'adp_parking.settings'
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", __file__)
import django
django.setup()


from django.contrib.auth import authenticate
from django.contrib import admin
# from django.contrib.auth.models import User
from .models import Usuario

from django.contrib.auth import get_user_model
from django.conf import settings
User = get_user_model()

file = 'file.csv'

data = csv.reader(open(file), delimiter=",")
for row in data:
    if row[0] != "Number":
        # Post.id = row[0]
        Post=Usuario()
        Post.drt = row[0]
        Post.nome = row[1]
        Post.cargo = row[2]
        Post.perfil_acesso = row[3]
        Post.save()


