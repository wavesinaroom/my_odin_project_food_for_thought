from django.urls import path
from . import views

urlpatterns = [
        path('level', views.choose_level, name='choose_level'),
        path('question', views.show_question, name='show_question'),
        path('success', views.notify_success, name='notify_success'),
        path('failure', views.notify_failure, name='notify_failure'),
        path('reward', views.choose_reward, name='choose_reward'),
        path('to_journal', views.redirect_to_journal, name='redirect_to_journal')
        ]
