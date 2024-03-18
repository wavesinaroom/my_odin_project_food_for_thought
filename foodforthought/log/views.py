from django.shortcuts import render
from django.template import loader
from .models import Log
import urllib.request
import json
import logging

def choose_level(request):
    return HttpResponse("NOT IMPLEMENTED: question level")

def show_question(request):
    url = 'https://opentdb.com/api.php?amount=1&category=9&difficulty=easy&type=multiple' 
    with urllib.request.urlopen(url) as response:
        res = json.loads(response.read())
        context = res["results"][0]
        return render(request, "log/question.html", context)
    
def notify_success(request):
    return HttpResponse("NOT IMPLEMENTED: success")

def notify_failure(request):
    return HttpResponse("NOT IMPLEMENTED: failure")

def choose_reward(request):
    return HttpResponse("NOT IMPLEMENTED: choose_reward")

def redirect_to_journal(request):
    return HttpResponse("NOT IMPLEMENTED: to_journal")

