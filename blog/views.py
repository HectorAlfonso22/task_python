from django.shortcuts import render
from django.shortcuts import redirect
from .models import Article
from .forms import ArticleForm


def index(request):
    articles = Article.objects.all()
    params = {
        'articles': articles,
    }
    return render(request, 'blog/index.html', params)


def create(request):
    if (request.method == 'POST'):
        obj = Article()
        article = ArticleForm(request.POST, instance=obj)
        article.save()
        return redirect('index')
    else:
        params = {
            'form': ArticleForm(),
        }
        return render(request, 'blog/create.html', params)


def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    params = {
        'article': article,
    }
    return render(request, 'blog/detail.html', params)


def edit(request, article_id):
    article = Article.objects.get(id=article_id)
    if (request.method == 'POST'):
        article = ArticleForm(request.POST, instance=article)
        article.save()
        return redirect('detail', article_id)
    else:
        params = {
            'article': article,
            'form': ArticleForm(instance=article),
        }
        return render(request, 'blog/edit.html', params)


def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    if (request.method == 'POST'):
        article.delete()
        return redirect('index')
    else:
        params = {
            'article': article,
        }
        return render(request, 'blog/delete.html', params)
