from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from usuario.models import Usuario
import logging


db_logger = logging.getLogger('django')

def template(request):
  db_logger.warning('warning message XPTO 3')
  mydata = Usuario.objects.all()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  db_logger.warning('warning message XPTO 4')
  return HttpResponse(template.render(context, request))


