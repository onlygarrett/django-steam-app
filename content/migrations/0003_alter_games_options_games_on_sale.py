# Generated by Django 4.1.5 on 2023-07-02 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_alter_genre_options_games'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='games',
            options={'ordering': ('name',), 'verbose_name_plural': 'Games'},
        ),
        migrations.AddField(
            model_name='games',
            name='on_sale',
            field=models.BooleanField(default=False),
        ),
    ]
