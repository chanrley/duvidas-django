from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from usuario.models import Usuario

def template(request):
  mydata = Usuario.objects.all()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))


