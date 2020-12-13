from django.http import HttpResponse
from django.shortcuts import render
from django.db.models.functions import Replace
from .models import Recipe
from .models import RecipeTable
from .forms import MacroForm

import django_tables2 as tables


def recipe_index(request):
    return render(request, 'recipes.html', {
        'recipes': Recipe.objects.using('recipe_database').all()
    })


def recipe_get(request, id_input):
    recipe_name = Recipe.objects.using('recipe_database').get(common_key_recipe=id_input).name
    return HttpResponse(recipe_name)


def recipe_by_id(request, id_input):
    return render(request, 'recipe_by_id.html', {
        'recipe': Recipe.objects.using('recipe_database').get(common_key_recipe=id_input),
        # 'ingredients': models.Ingredient.objects.using('recipe_database').get(common_key_recipe=recipe_id)
        'ingredients': Recipe.objects.using('recipe_database').get(common_key_recipe=id_input).ingredient_set.all()
    })


class TableView(tables.SingleTableView):
    model = Recipe.objects.using('recipe_database')
    table_class = RecipeTable
    template_name = 'recipes_table.html'
    queryset = Recipe.objects.using('recipe_database').all()


def lookup_by_macros(request):
    queryset = Recipe.objects.using('recipe_database').values('name')
    if request.method == 'POST':
        form = MacroForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = MacroForm()
    return render(request, 'lookup_by_macros.html', {
            'recipes': Recipe.objects.using('recipe_database').all(),
            'form': form
        })
