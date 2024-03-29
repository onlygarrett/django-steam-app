# Generated by Django 4.1.5 on 2023-07-10 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SteamTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Tags',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='SteamGames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('steam_appid', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('short_description', models.TextField(blank=True, null=True)),
                ('header_image', models.ImageField(blank=True, null=True, upload_to='item_images')),
                ('price', models.FloatField(default=0)),
                ('discount', models.FloatField(default=0)),
                ('on_sale', models.BooleanField(default=False)),
                ('developers', models.JSONField(default=list)),
                ('release_date', models.DateTimeField(blank=True, null=True)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='utility.steamtags')),
            ],
            options={
                'verbose_name_plural': 'SteamGames',
                'ordering': ('tag',),
            },
        ),
    ]
