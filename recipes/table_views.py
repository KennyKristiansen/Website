from recipes.models import Recipe, Nutrient
from recipes.models import RecipeTable, NutrientTable
import django_tables2 as tables


class TableView(tables.SingleTableView):
    model = Recipe.objects.using('recipe_database')
    table_class = RecipeTable
    template_name = 'recipes_table.html'
    queryset = Recipe.objects.using('recipe_database').all()
    # Remove splitting of tables over several sites
    tables.SingleTableView.table_pagination = False


class TableViewNutrients(tables.SingleTableView):
    model = Nutrient.objects.using('nutrient_database')
    table_class = NutrientTable
    template_name = 'recipes_table.html'
    queryset = Nutrient.objects.using('nutrient_database').all()
    # Remove splitting of tables over several sites
    tables.SingleTableView.table_pagination = False
