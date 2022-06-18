from django.shortcuts import render, redirect
from .models import *
from .scripts import *
# Create your views here


def home(request):
    teams = Team.objects.all()
    topics = Topic.objects.all()
    questions = Question.objects.all()

    counter = 10
    row_list = []
    while counter <= 50:
        single_row = []
        for topic in topics:
            found_state = False
            for question in questions:
                if question.topic == topic and question.question_points.value == counter:
                    single_row.append(question)
                    found_state = True
            if not found_state:
                single_row.append("no entry")
        row_list.append(single_row)
        counter += 10
    dates = {'teams': teams,
             'topics': topics,
             'questions': questions,
             'row_list': row_list}
    return render(request, 'sites/home.html', dates)


def question_by_id(request, id_number):
    teams = Team.objects.all()
    question = Question.objects.get(id=int(id_number))
    dates = {'question': question,
             'teams': teams,
             'id_number': id_number}
    if request.method == 'POST':
        log_team = None
        log_question = question
        for team in teams:
            if str(team.id) in request.POST:
                log_team = team
                team.point_status += question.question_points.value
                team.save()

        question.state = False
        question.save()
        next_team_change()
        return redirect('home')
    return render(request, 'sites/questions_by_id.html', dates)


def setup(request):
    teams = Team.objects.all()
    logs = Log.objects.all()[:10]
    dates = {'teams': teams,
             'logs': logs}
    if request.method == 'POST':
        if 'reset' in request.POST:
            reset_system()
        return redirect('setup')
    return render(request, 'sites/setup.html', dates)
