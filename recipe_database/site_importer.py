import os
import csv
import database_api as api
import bs4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import re


class Progress:

    def __init__(self):
        self.min = 0
        self.max = 0
        self.current = 0
        self.progress = 1

    def update(self):

        increments = float(int(self.max) - int(self.min)) / 100
        compare = self.progress * increments
        while self.current > compare:
            self.progress += 1
            compare = self.progress * increments
            percentage = compare / self.max * 100
            print(str(round(percentage, 2)) + ' %', end="\r")

        else:
            pass




unit_regex = re.compile(r'([0-9,.½¼]+)[\s](\S+)?')

test_ingredient_list = ['Skrubbede nye kartofler - evt. i halve og kvarte', 'Vand', 'Groft salt',
                        'Karolines Køkken® Kvark 0,3%',
                        'Fintrevet parmesanost eller Karolines Køkken® Pasta- & gratineringsost',
                        'Friske basilikumblade', 'Olivenolie', 'Groft salt', 'Cocktailtomater i halve',
                        'Dampede grønne bønner i mindre bidder', 'Sorte og grønne oliven', 'Havsalt',
                        'Friskkværnet peber', 'Friske basilikumblade', 'Rugbrød - evt. ristet']
test_ingredient_list = test_ingredient_list.sort()
os.chdir('''C:\\Users\\kenny\\PycharmProjects\\Python training\\Exercises\\recipe\\''')


def arla_import(html_link, recipe_id):
    # TODO: create unique id system
    recipe = api.Recipe()
    recipe.id = recipe_id
    recipe.link = html_link

    # driver setup
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(html_link)

    # wait until site is fully loaded
    try:
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(
            (By.CSS_SELECTOR, "div.u-mt--m:nth-child(1) > table:nth-child(2) > tbody:nth-child(1)")))
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(
            (By.CSS_SELECTOR, ".c-recipe__instructions-steps")))

    except TimeoutException:
        print(f'Timed out: {html_link}')

    web_page_unparsed = driver.page_source.encode('utf-8').strip()
    web_page = bs4.BeautifulSoup(web_page_unparsed, "lxml")
    recipe.name = (web_page.find('h1', attrs={'class': 'u-text-break u-mb--s u-mb--m@mobile'})).text
    recipe.description = (web_page.find('div', attrs={'class': 'c-recipe__description u-mt--s@mobile'})).text
    # recipe.export()
    # locate ingredient tables
    ingredients_list = []
    ingredient_tables = web_page.find_all('table')
    for table in ingredient_tables:
        ingredient_table = table.find_all('th')
        ingredient_unit = table.find_all('td')
        ingredient_and_unit_table = (list(zip(ingredient_table, ingredient_unit)))
        for ingredient, unit in ingredient_and_unit_table:
            ingredient_list = ingredient.find_all('span')
            unit = unit.text
            amount_unit = unit_regex.search(str(unit))
            if amount_unit is None:
                break
            amount = str(amount_unit[1])
            unit = str(amount_unit[2])

            # print('mængde: ' + amount + '  unit: ' + unit)
            try:
                ingredient_single = str(ingredient_list[-1].text)
                ingredient = api.Ingredient()
                ingredient.id = recipe_id
                    ingredient.ingredient = ingredient_single
                ingredient.amount = amount
                ingredient.unit = unit
                ingredient.export()
                # print(f'ingredient - {ingredient.ingredient} amount - {ingredient.amount} unit - {ingredient.unit}')

            except IndexError:
                macro_unit = (str(ingredient.text).replace(':', ''))
                if macro_unit == 'Protein':
                    recipe.protein = amount
                if macro_unit == 'Kulhydrat':
                    recipe.carbs = amount
                if macro_unit == 'Fedt':
                    recipe.fat = amount
                pass
    recipe.export()
    step_int = 0
    recipe_steps = web_page.find_all('ul', attrs='u-bare-list u-ml--m')
    for step in recipe_steps:
        step_api = api.Steps()
        step_list = step.find_all('span')
        try:
            step_description = str(step_list[-1].text)
            step_api.step = step_int
            step_api.description = step_description
            step_api.id = recipe_id
            step_int += 1
            step_api.export()
        except IndexError:
            pass

    ingredients_list = ingredients_list.sort()
    if ingredients_list == test_ingredient_list:
        pass
    else:
        # print('lists are not identical')
        pass

    driver.quit()


# arla_import('https://www.arla.dk/opskrifter/kartoffelsalat-med-bonner-og-ost/', 0)

# exit()

with open('arla_all.csv', newline='') as csv_file:
    id = 0
    progress = Progress()
    reader = csv.reader(csv_file, delimiter=',', quoting=0)
    # row_count = sum(1 for row in reader)
    row_count = 5279
    progress.max = row_count
    for row in reader:
        progress.update()
        try:
            arla_import(row[0], id)
            id += 1
        except AttributeError as e:
            print(f'Attribute error: {e}')
            print(f'Site: {row[0]}')
            pass

recipe = api.Recipe()
