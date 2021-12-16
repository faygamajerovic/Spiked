from django.urls import path
from. import views

urlpatterns = [
    path('', views.list_recipes, name='list-recipes'),
    # path('search', views.find, name='find'),
]