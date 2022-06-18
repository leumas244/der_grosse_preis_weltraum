from colorfield.fields import ColorField
from django.db import models

action_choices = [('closed', 'geschlossen'),
                  ('open', 'geöffnet'),
                  ]

question_categories = [('Frage', 'Frage'),
                       ('Schätzfrage', 'Schätzfrage'),
                       ('Aktion', 'Aktion'),
                       ('Battle', 'Battle'),
                       ('Joker', 'Joker'),
                       ]

# Create your models here.
class Team(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField('Name', max_length=40, blank=True)

    color = ColorField('Farbe', default='#FF0000', unique=True)

    point_status = models.IntegerField('Punktestand', default=0)

    is_active = models.BooleanField('An der Reihe', default=False)

    update_date = models.DateTimeField('Aenderungsdatum', auto_now=True)

    def __str__(self):
        return self.name


class Topic(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField('Name', max_length=40, blank=True)

    update_date = models.DateTimeField('Aenderungsdatum', auto_now=True)

    def __str__(self):
        return self.name


class Point(models.Model):
    id = models.AutoField(primary_key=True)

    value = models.IntegerField('Wert', unique=True)

    update_date = models.DateTimeField('Aenderungsdatum', auto_now=True)

    def __str__(self):
        return str(self.value)


class Question(models.Model):
    id = models.AutoField(primary_key=True)

    question_points = models.ForeignKey(Point, on_delete=models.CASCADE)

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    question_category = models.CharField('Kategorie', max_length=40, choices=question_categories, default='Frage')

    name = models.CharField('Name', max_length=240, blank=True)

    solution = models.CharField('Loesung', max_length=240, blank=True)

    state = models.BooleanField('Aktiv?', default=True)

    update_date = models.DateTimeField('Aenderungsdatum', auto_now=True)

    def __str__(self):
        return '%s %s' % (self.topic, self.question_points)

    class Meta:
        unique_together = ('question_points', 'topic')


class Log(models.Model):
    id = models.AutoField(primary_key=True)

    affected_team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True)

    affected_question = models.ForeignKey(Question, on_delete=models.CASCADE)

    action = models.CharField('Aktion', max_length=240, choices=action_choices)

    rollback = models.BooleanField('Rückgängig gemacht?', default=False)

    update_date = models.DateTimeField('Aenderungsdatum', auto_now=True)

    creation_date = models.DateTimeField('Erstellungsdatum', auto_now_add=True)
