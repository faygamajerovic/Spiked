# Generated by Django 4.0 on 2021-12-21 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0002_glass'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spirit',
            name='photo',
        ),
    ]