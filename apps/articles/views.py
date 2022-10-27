from django.shortcuts import render, redirect
from .models import Article, Tags, Category
from apps.comments.forms import CommentForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def index(request):
    object_list = Article.objects.all().order_by('-id')

    context = {
        'object_list': object_list
    }

    return render(request, 'index.html', context)


def views_up(request, pk):
    article = Article.objects.get(id=pk)
    article.views += 1
    article.save()
    return redirect('articles:single', article.pk)


def article_single(request, pk):
    article = Article.objects.get(id=pk)
    categories = Category.objects.all()
    recent_articles = Article.objects.all().order_by('-id')[:3]
    tags = Tags.objects.all()

    form = CommentForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.article_id = pk
        obj.save()
        return redirect(f'/blog-detail/{pk}#article-comments')
    context = {
        'object': article,
        'categories': categories,
        'recent_articles': recent_articles,
        'tags': tags,
        'form': form,
    }
    return render(request, 'blog-single.html', context)


def article_view(request):
    articles = Article.objects.all().order_by('-id')

    tag = request.GET.get('tag')
    category = request.GET.get('category')
    q = request.GET.get('q')
    page_number = request.GET.get('page')

    if q:
        articles = articles.filter(title__icontains=q)
    if tag:
        articles = articles.filter(tags__title__exact=tag)
    if category:
        articles = articles.filter(category__title__exact=category)


    p = Paginator(articles, 1)
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)

    context = {
        'object_list': articles,
        'page_obj': page_obj,
    }
    return render(request, 'blog.html', context)
