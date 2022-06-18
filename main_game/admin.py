from django.contrib import admin
from .models import *


# Register your models here.
class LogAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'affected_team',
                    'affected_question',
                    'action',
                    'rollback',
                    'update_date',
                    'creation_date']


class PointAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'value',
                    'update_date']


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'question_points',
                    'topic',
                    'question_category',
                    'name',
                    'solution',
                    'state',
                    'update_date']


class TeamAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'name',
                    'color',
                    'point_status',
                    'is_active',
                    'update_date']


class TopicAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'name',
                    'update_date']


admin.site.register(Log, LogAdmin)
admin.site.register(Point, PointAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Topic, TopicAdmin)
