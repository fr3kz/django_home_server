# Generated by Django 2.1.4 on 2018-12-07 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_file_prifle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='prifle',
            new_name='prile',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='files',
        ),
    ]