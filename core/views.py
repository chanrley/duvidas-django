from django.shortcuts import render, redirect, get_object_or_404

from item.models import Category, Item
from .forms import SignupForm
from django.db import models
from novo_portal_dva.models import models, Menu, SubMenu

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

def nova_url(request):
    categories = Category.objects.all()
    return render(request, 'core/nova_url.html', {
        'categories': categories
    })

def master(request):
    categories = Category.objects.all()
    return render(request, 'core/master.html', {
        'categories': categories
    })

def navbar(request):
    menus = Menu.objects.all()
    submenus = SubMenu.objects.all()
    #sub = get_object_or_404(SubMenu, pk=id)

    return render(request, 'core/navbar.html', {
        'menus': menus,
        'submenus': submenus,
        #'sub': sub
    })

def navbar_teste(request):
    menus = Menu.objects.all()
    submenus = SubMenu.objects.all()
    #sub = get_object_or_404(SubMenu, pk=id)

    return render(request, 'core/navbar_teste.html', {
        'menus': menus,
        'submenus': submenus,
        #'sub': sub
    })


