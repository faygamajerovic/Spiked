from django.db import models
from accounts.models import Profile
from django.db.models.aggregates import Max

# Create your models here.


class Query(models.Model):
    search_string = models.CharField(max_length=255, null=True, blank=True, unique=True)

    def __str__(self) -> str:
        return self.search_string
    

class Ingredient(models.Model):

    name = models.CharField(max_length=255, null=True, blank=True, unique=True)

    def __str__(self) -> str:
        return self.name


class Recipe(models.Model):

    api_recipe_id = models.CharField(max_length=20, null=False, blank=False)

    name = models.CharField(max_length=255, null=True, blank=True)

    glass = models.CharField(max_length=255, null=True, blank=True)

    instructions = models.TextField(null=True, blank=True)

    thumbnail = models.CharField(max_length=500, null=True, blank=True)

    ingredients = models.ManyToManyField(Ingredient, related_name="recipes")
    

    is_completed = models.BooleanField(null=True, default=False)


    def __str__(self) -> str:
        return str(self.api_recipe_id)+ "  |  " +self.name


class UserRecipe(models.Model):

    name = models.CharField(max_length=255, null=True, blank=True)
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d')
    glass = models.CharField(max_length=255, null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredient, related_name="user_recipes")
    instructions = models.TextField(null=True, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="my_recipes", null=True)

    def __str__(self) -> str:
        return self.name