# Generated by Django 4.1.5 on 2023-07-11 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_alter_games_developers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='developers',
            field=models.ManyToManyField(related_name='developers', to='content.developer'),
        ),
    ]
