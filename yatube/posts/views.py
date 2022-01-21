# from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    title = 'Последние обновления на сайте'
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'title': title,
        'posts': posts
    }
    return render(request, template, context)


def group_posts(request, slug):
    title = 'Лев Толстой – зеркало русской революции.'
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'title': title,
        'group': group,
        'posts': posts
    }
    return render(request, template, context)
