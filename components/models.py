from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]


class Spirit (models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    description = models.TextField(blank=True)
    classification = models.CharField(max_length=200)
    alcohol_content = models.DecimalField(max_digits=5, decimal_places=0, validators=PERCENTAGE_VALIDATOR)
    famous_distillers = models.CharField(max_length=200)
    styles = models.CharField(max_length=200)

    def __str__(self):
        return self.name
