# Generated by Django 2.2.6 on 2019-12-20 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20191220_1828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='team_id',
        ),
        migrations.AlterField(
            model_name='team',
            name='winner',
            field=models.BooleanField(default='False'),
        ),
    ]
