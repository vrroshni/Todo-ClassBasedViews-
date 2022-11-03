from django.shortcuts import render
from .models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.
class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'ClssBasedViews/tasks.html'



class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'ClssBasedViews/task.html'

    