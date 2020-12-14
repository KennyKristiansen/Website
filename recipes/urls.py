"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

import views
import table_views
import django_tables2 as tables

urlpatterns = [
    path('', views.recipe_index, name='recipe_index'),
    path('<int:id_input>', views.recipe_by_id, name='recipe_id_get'),
    path('macros', views.lookup_by_macros, name='lookup_by_macros'),
    path('table', table_views.TableView.as_view(), name='tables_view')

]
