# Generated by Django 3.2.5 on 2021-07-16 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_game', '0008_auto_20210630_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='An der Reihe'),
        ),
    ]
