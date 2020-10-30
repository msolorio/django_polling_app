from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(request):
    last_five_questions = Question.objects.order_by('-pub_date')[:5]

    return render(request, './polls/index.html', { 'questions': last_five_questions })


def detail(request, question_id):
    return HttpResponse(f'You\'re looking at question {question_id}')


def results(request, question_id):
    return HttpResponse(f'You\'re looking at the results of {question_id}')


def vote(request, question_id):
    return HttpResponse(f'You\'re voting on question {question_id}')


# def results(request, question_id):
#     return HttpResponse(f'')