from django.shortcuts import render, HttpResponse
from django.template import loader
from .forms import QuestionLevelForm

def process_question(request):
    if 'level' in request.POST:
        return HttpResponse('NOT IMPLEMENTED: Fetch trivia question')
    elif 'answer' in request.POST:
        return HttpResponse('NOT IMPLEMENTED: Check answer')
    else: 
        form = QuestionLevelForm();

    return render(request, "log/question.html", {"form": form})
