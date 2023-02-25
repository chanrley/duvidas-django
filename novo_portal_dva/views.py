from django.shortcuts import render, get_object_or_404
from . import views

def index(request):
    return render(request, "index.html")


