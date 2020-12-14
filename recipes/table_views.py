from recipes.models import Recipe
from recipes.models import RecipeTable
import django_tables2 as tables

class TableView(tables.SingleTableView):
    model = Recipe.objects.using('recipe_database')
    table_class = RecipeTable
    template_name = 'recipes_table.html'
    queryset = Recipe.objects.using('recipe_database').all()
    # Remove splitting of tables over several sites
    tables.SingleTableView.table_pagination = False

