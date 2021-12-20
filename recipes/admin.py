from django.contrib import admin

# Register your models here.

from . import models


admin.site.register(models.Ingredient)

admin.site.register(models.Recipe)

admin.site.register(models.UserRecipe)

admin.site.register(models.Profile)

admin.site.register(models.Query)