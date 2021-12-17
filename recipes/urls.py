from django.urls import path
from. import views

urlpatterns = [
    path('', views.list_recipes, name='list-recipes'),
    path('newrecipe', views.user_recipe, name='user_recipe')
    # path('search', views.find, name='find'),
]