# Generated by Django 2.1.4 on 2018-12-07 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='files',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.File'),
        ),
    ]
