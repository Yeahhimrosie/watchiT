# Generated by Django 2.2 on 2021-04-16 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watchApp', '0002_movie_watchd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='liked_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_that_liked', to='watchApp.User'),
        ),
    ]
