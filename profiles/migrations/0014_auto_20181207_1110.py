# Generated by Django 2.1.4 on 2018-12-07 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_auto_20181207_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='files',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]