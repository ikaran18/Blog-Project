# Generated by Django 4.1.7 on 2023-04-26 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartoon',
            old_name='description1',
            new_name='download',
        ),
        migrations.RenameField(
            model_name='cartoon',
            old_name='description2',
            new_name='download1',
        ),
        migrations.RenameField(
            model_name='cartoon',
            old_name='description3',
            new_name='download2',
        ),
        migrations.RenameField(
            model_name='cartoon',
            old_name='description4',
            new_name='download3',
        ),
        migrations.RenameField(
            model_name='cartoon',
            old_name='title1',
            new_name='text',
        ),
    ]