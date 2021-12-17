from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Recipe, UserRecipe
from.forms import RecipeForm
# Create your views here.
# def find(request):
#     return HttpResponse("Search Worked")


def list_recipes(request):

    from .requestapi import random_recipe

    data = random_recipe()
    drinks = data.get("drinks")[0]

    api_recipe_id = drinks.get("idDrink")
    name = drinks.get("strDrink")
    glass = drinks.get("strGlass")
    image = drinks.get("strDrinkThumb")
    instructions = drinks.get("strInstructions")

    new_recipe = Recipe(api_recipe_id=api_recipe_id, name=name, glass=glass, instructions=instructions, thumbnail=image)
    new_recipe.save()

    print(api_recipe_id, name, glass, instructions)

    # Recipe.objects.create()


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
            form.save()

            return redirect('dashboard')
    else:
        form = RecipeForm()
    return render(request, 'pages/newrecipe.html', {'form': form})