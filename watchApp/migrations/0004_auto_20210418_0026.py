# Generated by Django 2.2 on 2021-04-18 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchApp', '0003_auto_20210415_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
