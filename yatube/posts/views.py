from django.shortcuts import render, get_object_or_404
from .models import Post, Group


# модуль отвечающий за главную страницу
def index(request):
    # сохраняем выборку из БД в переменную
    posts = Post.objects.order_by('-pub_date')[:10]

    # Из словаря context отправляем информацию в шаблон
    context = {
        'posts': posts,
        'title': 'Последние обновления сайта.'
    }
    # вывод значений в html шаблон
    return render(request, 'posts/index.html', context)


# модуль отвечающий за страницу сообщества
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    # сохраняем выборку в соответствии с id группы
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
        'title': f'Записи сообщества {slug}',
    }
    return render(request, 'posts/group_list.html', context)
