# Generated by Django 4.0 on 2021-12-15 17:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spirit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
                ('classification', models.CharField(max_length=200)),
                ('alcohol_content', models.DecimalField(decimal_places=0, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('famous_distillers', models.CharField(max_length=200)),
                ('styles', models.CharField(max_length=200)),
            ],
        ),
    ]
