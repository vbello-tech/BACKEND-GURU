# Generated by Django 4.2.1 on 2023-06-08 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(default='zoovcs4oaf'),
        ),
    ]