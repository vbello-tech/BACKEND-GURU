# Generated by Django 4.2.1 on 2023-05-30 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='published_date',
            new_name='posted_date',
        ),
    ]
