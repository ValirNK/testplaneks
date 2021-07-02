from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Musician


def index(request):
    context = {'latest_question_list': 'dsf323'}
    return render(request, 'index.html', context)

class Login(LoginRequiredMixin, ListView):
    model = Musician
    template_name = 'index.html'