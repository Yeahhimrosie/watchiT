# Generated by Django 2.2 on 2021-04-19 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchApp', '0007_auto_20210418_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
