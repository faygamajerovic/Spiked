from django.contrib import admin

# Register your models here.

from .models import Spirit, Glass

admin.site.register(Spirit)
admin.site.register(Glass)
