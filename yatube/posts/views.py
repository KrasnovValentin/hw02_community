from django.shortcuts import render, get_object_or_404
from .models import Post, Group


# модуль отвечающий за главную страницу
def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]  # сохраняем выборку из БД в переменную
    context = {
        'posts': posts,  # Из словаря context отправляем информацию в шаблон
        'title': 'Последние обновления сайта.'
    }
    return render(request, 'posts/index.html', context)  # вывод значений в html шаблон


# модуль отвечающий за страницу сообщества
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]  # сохраняем выборку
    context = {  # в соответствии с id группы
        'group': group,
        'posts': posts,
        'title': f'Записи сообщества {slug}',
    }
    return render(request, 'posts/group_list.html', context)
