# Generated by Django 4.2.11 on 2024-03-13 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_ingredients', models.JSONField()),
                ('recipe_area', models.JSONField()),
                ('recipe_categories', models.JSONField()),
                ('activities', models.JSONField()),
            ],
        ),
    ]
