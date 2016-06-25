from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from . models import HomepageArticle


def index(request):
    articles = HomepageArticle.objects.all()
    return render(request, 'home/index.html', {'articles': articles})


def article(request, article_id):
    article = get_object_or_404(HomepageArticle, pk=article_id)
    return render(request, 'home/article.html', {'article': article})
