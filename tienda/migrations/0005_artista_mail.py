# Generated by Django 3.0.2 on 2020-01-13 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0004_auto_20200113_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='artista',
            name='mail',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
