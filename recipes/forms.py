from django import forms

from .models import UserRecipe, Ingredient
from django.forms import ModelForm, Select, CheckboxSelectMultiple, SelectMultiple


class RecipeForm(ModelForm):
    class Meta:
        model = UserRecipe
        fields = ['name', 'glass', 'ingredients', 'instructions', 'image']
        widgets = {
            'ingredients': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'glass': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'instructions': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }