from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from requests import request

from recipes.helper import ingredients_processor
from .models import Ingredient, Query, Recipe, UserRecipe
from.forms import RecipeForm
# Create your views here.
# def find(request):
#     return HttpResponse("Search Worked")


def single_recipe_from_db(request, id):

    from .requestapi import full_cocktail_details

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


def search_by_ingredients(request):
    ingredient1 = request.GET.get("ingredient1")
    ingredient2 = request.GET.get("ingredient2")
    ingredient3 = request.GET.get("ingredient3")

    print(ingredient1, ingredient2, ingredient3)

    #rum, lemon, whisky

    ingredient_list = []

    if ingredient1 is not "":
        ingredient_list.append(ingredient1)

    if ingredient2 is not "":
        ingredient_list.append(ingredient2)

    if ingredient3 is not "":
        ingredient_list.append(ingredient3)


    try:
        query_search_string = Query.objects.get(search_string=str(ingredient_list)).exist()
    except:
        query_search_string = False
    
    if query_search_string is False:

        from .requestapi import filter_by_ingredients

        data = filter_by_ingredients(ingredient_list)


        drinks = data.get("drinks")


        for drink in drinks:


            print("Current > ",drink)

            api_drink_id = drink.get("idDrink")
            image = drink.get("strDrinkThumb")
            name = drink.get("strDrink")
            print(api_drink_id, image, name)

            query = Recipe.objects.filter(api_recipe_id=api_drink_id).exists()

            print(query)

            if query:
                continue

            else:
                recipe = Recipe(api_recipe_id=api_drink_id, name=name, thumbnail=image, is_completed=False)

                recipe.save()

        query_instance = Query(search_string=str(ingredient_list))
        query_instance.save()

    

    
    query = Recipe.objects.filter(ingredients__in=ingredient_list)

    context = {
        "recipes" : query
    }
    

    return render(request, "pages/search_by_ingredients.html", context=context)


def list_recipes(request):

    # from .requestapi import random_recipe

    # data = random_recipe()
    # drinks = data.get("drinks")[0]

    # api_recipe_id = drinks.get("idDrink")
    # name = drinks.get("strDrink")
    # glass = drinks.get("strGlass")
    # image = drinks.get("strDrinkThumb")
    # instructions = drinks.get("strInstructions")

    # new_recipe = Recipe(api_recipe_id=api_recipe_id, name=name, glass=glass, instructions=instructions, thumbnail=image)
    # new_recipe.save()

    # print(api_recipe_id, name, glass, instructions)

    search_query = request.GET.get("search")

    if search_query is not None:
        query_results = Recipe.objects.filter(name__contains=search_query)
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


