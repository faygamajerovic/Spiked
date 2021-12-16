from django.db import models
from django.db.models.aggregates import Max

# Create your models here.



    

class Ingredient(models.Model):

    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Recipe(models.Model):

    api_recipe_id = models.CharField(max_length=20, null=False, blank=False)


    name = models.CharField(max_length=255, null=True, blank=True)

    glass = models.CharField(max_length=255, null=True, blank=True)

    instructions = models.TextField(null=True, blank=True)


    thumbnail = models.CharField(max_length=500,null=True, blank=True)

    ingredients = models.ManyToManyField(Ingredient, related_name="recipes")

    def __str__(self) -> str:
        return self.name