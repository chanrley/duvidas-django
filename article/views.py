from django.shortcuts import render, HttpResponse, redirect
from .models import Article
from .forms import ArticleForm


def index(request):
    # return HttpResponse("<h1>Foi</h1>")
    articles = Article.objects.all()
    return render(request, 'article/index.html', {'articles': articles})

def detail(request, id):
    article = Article.objects.get(pk=id)

    if request.method =='POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('../')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'article/detail.html', {'article': article, 'form': form})
    
