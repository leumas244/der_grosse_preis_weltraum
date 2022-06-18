from .models import *


def next_team_change():
    sequence = [1, 2, 3, 4]
    active_team = Team.objects.get(id=1)

    teams = Team.objects.all()
    for team in teams:
        if team.is_active:
            active_team = team

    list_order_active = sequence.index(active_team.id)
    next_list_element = list_order_active + 1
    if next_list_element >= len(sequence):
        next_list_element = 0

    next_team = Team.objects.get(id=sequence[next_list_element])

    active_team.is_active = False
    next_team.is_active = True

    active_team.save()
    next_team.save()
    return


def reset_system():
    teams = Team.objects.all()
    questions = Question.objects.all()

    for team in teams:
        team.point_status = 0
        if team.id == 1:
            team.is_active = True
        else:
            team.is_active = False
        team.save()

    for question in questions:
        question.state = True
        question.save()

    return
