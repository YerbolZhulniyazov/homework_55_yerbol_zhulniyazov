from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from webapp.models import TODO


def index_view(request: WSGIRequest):
    tasks = TODO.objects.exclude(is_deleted=True)
    context = {
        'tasks': tasks
    }
    return render(request, 'index.html', context=context)
