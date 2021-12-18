from django.urls import path
from. import views

urlpatterns = [
    path('', views.list_recipes, name='list_recipes'),
    path("detail/<id>", views.single_recipe_from_db, name="single_recipe"),
    path("search_by_ingredients/", views.search_by_ingredients, name="search_by_ingredients"),
    path('newrecipe', views.user_recipe, name='user_recipe')
    # path('search', views.find, name='find'),
]