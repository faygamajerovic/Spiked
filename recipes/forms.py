from .models import UserRecipe
from django.forms import ModelForm


class RecipeForm(ModelForm):
    class Meta:
        model = UserRecipe
        fields = "__all__"