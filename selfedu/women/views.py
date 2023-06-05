from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("Страница приложения Women")

def categories(request, cats):
    if int(cats)>3:
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1>Статьи по категориям:</h1><p>{cats}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена")