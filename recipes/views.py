from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from requests import request
from django.db.models import Q, query
from recipes import requestapi

from recipes.helper import ingredients_processor
from .models import Ingredient, Query, Recipe, UserRecipe
from.forms import RecipeForm


from .requestapi import full_cocktail_details, filter_by_ingredients

def single_recipe_from_db(request, id):

    recipe = Recipe.objects.get(id=id)

    if recipe.is_completed == False:

        data = full_cocktail_details(recipe.api_recipe_id)

        drinks = data.get("drinks")[0]

        ingredients_list = ingredients_processor(drinks)

        list_of_ingredients_objects = []

        for ingredient in ingredients_list:
            ingredient_instance = Ingredient(name=ingredient)

            try:
                ingredient_instance.save()
                list_of_ingredients_objects.append(ingredient_instance)
            except IntegrityError:
                ingredient_instance = Ingredient.objects.get(name=ingredient)
                list_of_ingredients_objects.append(ingredient_instance)

        glass = drinks.get("strGlass")
        image = drinks.get("strDrinkThumb")
        instructions = drinks.get("strInstructions")

        recipe.glass = glass
        recipe.instructions = instructions
        recipe.ingredients.add(*list_of_ingredients_objects)
        recipe.is_completed = True
        recipe.save()
        # print(data)

    context = {
        "recipe": recipe
    }

    return render(request, "pages/single_recipe_detail.html", context=context)


def search_by_ingredients_in_api(ingredient_list):


    data = filter_by_ingredients(ingredient_list)

    drinks = data.get("drinks")

    for drink in drinks:

        print("Current > ", drink)

        api_drink_id = drink.get("idDrink")
        image = drink.get("strDrinkThumb")
        name = drink.get("strDrink")
        print(api_drink_id, image, name)

        query = Recipe.objects.filter(api_recipe_id=api_drink_id).exists()

        print(query)

        if query:
            continue

        else:
            recipe = Recipe(api_recipe_id=api_drink_id, name=name, thumbnail=image)

            recipe.save()

            data = full_cocktail_details(recipe.api_recipe_id)

            drinks = data.get("drinks")[0]

            ingredients_list = ingredients_processor(drinks)

            list_of_ingredients_objects = []

            for ingredient in ingredients_list:
                
                try:
                    ingredient_instance = Ingredient(name=ingredient)
                    ingredient_instance.save()
                    list_of_ingredients_objects.append(ingredient_instance)
                except IntegrityError:
                    ingredient_instance = Ingredient.objects.get(name=ingredient)
                    list_of_ingredients_objects.append(ingredient_instance)

            glass = drinks.get("strGlass")
            instructions = drinks.get("strInstructions")

            recipe.glass = glass
            recipe.instructions = instructions
            recipe.ingredients.add(*list_of_ingredients_objects)
            recipe.is_completed = True
            recipe.save()


def list_recipes(request):

    ingredient1 = request.GET.get("ingredient1")
    ingredient2 = request.GET.get("ingredient2")
    ingredient3 = request.GET.get("ingredient3")
    search_query = request.GET.get("search")

    # print(ingredient1, ingredient2, ingredient3)

    ingredient_list = []

    if ingredient1 is not "":
        ingredient_list.append(ingredient1)

    if ingredient2 is not "":
        ingredient_list.append(ingredient2)

    if ingredient3 is not "":
        ingredient_list.append(ingredient3)

    ingredient_list = [str(ingredient).capitalize()
                       for ingredient in ingredient_list]

    # print(ingredient_list)

    # query = Recipe.objects.filter(ingredients__name__in=ingredient_list).distinct('name')
    # query = Recipe.objects.filter()

    if search_query is not None:
        query_results = Recipe.objects.filter(name__contains=search_query)

    elif ingredient1 is not None or ingredient2 is not None or ingredient3 is not None:

        try:
            query_results = Recipe.objects.filter(
                    ingredients__name__in=ingredient_list)

            if len(query_results) == 0:
                # print("Yes not found in the db go for api")
                search_by_ingredients_in_api(ingredient_list=ingredient_list)
                return redirect(request.get_full_path())
            # return redirect()
        except AttributeError as e:
            pass

    else:
        query_results = Recipe.objects.filter()

    context = {
        "recipes": query_results
    }
    return render(request, "pages/list_recipes.html", context=context)


def user_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            new_recipe = form.save()
            new_recipe.profile = request.user.profile
            new_recipe.save()
            return redirect('user_recipes')
        else:
            return render(request, 'pages/newrecipe.html', {'form': form})

    else:
        form = RecipeForm()
    return render(request, 'pages/newrecipe.html', {'form': form})


def myrecipe_list(request):

    return render(request, 'pages/my_recipes.html',)


def random_recipe(request):

    from .requestapi import random_recipe

    data = random_recipe()
    drinks = data.get("drinks")[0]

    # print("Here", drinks)

    ingredients_list = ingredients_processor(drinks)

    list_of_ingredients_objects = []

    for ingredient in ingredients_list:
        ingredient_instance = Ingredient(name=ingredient)

        try:
            ingredient_instance.save()
            list_of_ingredients_objects.append(ingredient_instance)
        except IntegrityError:
            ingredient_instance = Ingredient.objects.get(name=ingredient)
            list_of_ingredients_objects.append(ingredient_instance)

    api_recipe_id = drinks.get("idDrink")
    name = drinks.get("strDrink")
    glass = drinks.get("strGlass")
    image = drinks.get("strDrinkThumb")
    instructions = drinks.get("strInstructions")

    new_recipe = Recipe(api_recipe_id=api_recipe_id, name=name,
                        glass=glass, instructions=instructions, thumbnail=image)

    new_recipe.save()

    new_recipe.ingredients.add(*list_of_ingredients_objects)

    new_recipe.save()

    # new_recipe.ingredients.add(*list_of_ingredients_objects)

    # print(api_recipe_id, name, glass, instructions)

    context = {
        "recipe": new_recipe
    }

    return render(request, "pages/single_recipe_detail.html", context=context)

