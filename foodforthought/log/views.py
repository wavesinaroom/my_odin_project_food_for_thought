from django.shortcuts import render, HttpResponse
from .models import Log
import logging

logger = logging.getLogger(__name__)

def choose_level(request):
    return HttpResponse("NOT IMPLEMENTED: choose_level")

def show_question(request):
    return HttpResponse("NOT IMPLEMENTED: question")

def notify_success(request):
    return HttpResponse("NOT IMPLEMENTED: success")

def notify_failure(request):
    return HttpResponse("NOT IMPLEMENTED: failure")

def choose_reward(request):
    return HttpResponse("NOT IMPLEMENTED: choose_reward")

def redirect_to_journal(request):
    return HttpResponse("NOT IMPLEMENTED: to_journal")

