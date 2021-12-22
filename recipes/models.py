from django.contrib.auth.models import User
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

    favorites = models.ManyToManyField(Profile, default=None, blank=True, related_name="favorites")

    is_completed = models.BooleanField(null=True, default=False)


    def __str__(self) -> str:
        return str(self.api_recipe_id)+ "  |  " +self.name


class UserRecipe(models.Model):

    name = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(null=True, upload_to='pictures/')
    glass = models.CharField(max_length=255, null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredient, related_name="user_recipes")
    instructions = models.TextField(null=True, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="my_recipes", null=True)

    def __str__(self) -> str:
        return self.name

    def pic(self):
        if self.image:
            return self.image.url
        return "https://images.pexels.com/photos/3323682/pexels-photo-3323682.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"