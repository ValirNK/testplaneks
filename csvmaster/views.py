from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def index(request):
    context = {'latest_question_list': 'dsf323'}
    return render(request, 'index.html', context)