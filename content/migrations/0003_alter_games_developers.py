# Generated by Django 4.1.5 on 2023-07-11 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_remove_games_developers_games_developers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='developers',
            field=models.ManyToManyField(null=True, related_name='developers', to='content.developer'),
        ),
    ]
