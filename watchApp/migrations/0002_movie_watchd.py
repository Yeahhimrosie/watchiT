# Generated by Django 2.2 on 2021-04-16 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='watchd',
            field=models.BooleanField(default=False),
        ),
    ]
