from django.urls import path
from . import views

urlpatterns = [
        path('question', views.process_question, name='process_question'),
        ]
