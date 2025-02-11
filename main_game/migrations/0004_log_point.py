# Generated by Django 3.2.3 on 2021-05-31 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_game', '0003_question_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.IntegerField(unique=True, verbose_name='Wert')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Aenderungsdatum')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Aenderungsdatum')),
                ('affected_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_game.question')),
                ('affected_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_game.team')),
            ],
        ),
    ]
