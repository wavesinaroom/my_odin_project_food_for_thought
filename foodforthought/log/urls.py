from django.urls import path
from . import views

urlpatterns = [
        path('trivia/', views.fetch_trivia_question, name='fetch_trivia_question'),
        path('answer/', views.check_answer, name='check_answer'),
        path('reward/', views.check_reward_choice, name='check_reward_choice'),
        path('activity/', views.award_activity, name='views.award_activity'),
        ]
