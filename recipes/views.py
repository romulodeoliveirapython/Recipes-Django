from django.shortcuts import render
from .models import Recipe


def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request,
    'recipes/pages/home.html',
    context = {
        'recipes': recipes,
    }
)


def category(request, category_id):
    recipes = Recipe.objects.filter(category__id = category_id).order_by('-id')
    return render(request,
    'recipes/pages/home.html',
    context = {
        'recipes': recipes,
    }
)


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html')