from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('question/<int:id_number>/', views.question_by_id, name='question_by_id'),
    path('setup/', views.setup, name='setup'),
]
