# Generated by Django 3.2.5 on 2021-07-16 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_game', '0009_team_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='affected_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_game.team'),
        ),
    ]
