from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import TODOForm
from webapp.models import TODO


def add_view(request: WSGIRequest):
    if request.method == 'GET':
        form = TODOForm()
        return render(request, 'task_create.html', context={'form': form})

    form = TODOForm(data=request.POST)
    if form.is_valid():
        task = TODO.objects.create(
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            detailed_description=form.cleaned_data['detailed_description'],
            status=form.cleaned_data['status'],
            completion_date=form.cleaned_data['completion_date'])

        return redirect('detail_task', pk=task.pk)
    else:
        return render(request, 'task_create.html', context={'form': form})


def detail_view(request, pk):
    task = get_object_or_404(TODO, pk=pk)
    return render(request, 'task.html', context={
        'task': task
    })


def update_view(request, pk):
    task = get_object_or_404(TODO, pk=pk)
    if request.method == 'GET':
        form = TODOForm(initial={
            'title': task.title,
            'description': task.description,
            'detailed_description': task.detailed_description,
            'status': task.status,
            'completion_date': task.completion_date
        })
        return render(request, 'task_update.html', context={'form': form, 'task': task})
    form = TODOForm(data=request.POST)
    if form.is_valid():
        task.title = form.cleaned_data['title']
        task.description = form.cleaned_data['description']
        task.detailed_description = form.cleaned_data['detailed_description']
        task.status = form.cleaned_data['status']
        task.completion_date = form.cleaned_data['completion_date']
        task.save()
        return redirect('detail_task', pk=task.pk)
    else:
        return render(request, 'task_update.html', context={'form': form, 'task': task})


def delete_view(request, pk):
    task = get_object_or_404(TODO, pk=pk)
    return render(request, 'confirm_delete.html', context={'task': task})


def confirm_delete(request, pk):
    task = get_object_or_404(TODO, pk=pk)
    task.delete()
    return redirect('index')
