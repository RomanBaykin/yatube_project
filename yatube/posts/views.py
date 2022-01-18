# from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("This is our main page")


def group_posts(request, slug):
    return HttpResponse(f'Здесь будет находится ваш с пост со '
                        f'следующим названием {slug}')
