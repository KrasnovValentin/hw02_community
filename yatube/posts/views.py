from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from posts.models import Post, Group


def index(request: HttpRequest) -> HttpResponse:
    """Модуль отвечающий за главную страницу"""
    posts: str = Post.objects.all()[:10]
    context: dict = {
        'posts': posts,
        'title': 'Последние обновления сайта.'
    }
    return render(request, 'posts/index.html', context)


def group_posts(request: HttpRequest, slug: str) -> HttpResponse:
    """Модуль отвечающий за страницу сообщества"""
    group = get_object_or_404(Group, slug=slug)
    posts: str = Post.objects.filter(group=group)[:10]
    context: dict = {
        'group': group,
        'posts': posts,
        'title': f'Записи сообщества {slug}',
    }
    return render(request, 'posts/group_list.html', context)
