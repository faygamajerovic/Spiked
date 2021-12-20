from django import forms

from .models import UserRecipe, Ingredient
from django.forms import ModelForm, Select, CheckboxSelectMultiple


class RecipeForm(ModelForm):
    class Meta:
        model = UserRecipe
        fields = ['name', 'thumbnail', 'glass', 'ingredients', 'instructions']
        widgets = {'ingredients': CheckboxSelectMultiple()}