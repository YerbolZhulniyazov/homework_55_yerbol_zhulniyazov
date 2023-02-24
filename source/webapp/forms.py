from django import forms
from django.db.models import TextChoices

from django.forms import widgets


class StatusChoice(TextChoices):
    NEW = 'NEW', 'Новая'
    IN_PROGRESS = 'IN_PROGRESS', 'В прогрессе'
    COMPLETED = 'COMPLETED', 'Выполнена'


class TODOForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label='Задача')

    description = forms.CharField(max_length=100, required=True, label='Описание')

    detailed_description = forms.CharField(max_length=1000, required=True, label='Подробное описание',

                                           widget=widgets.Textarea)
    completion_date = forms.CharField(max_length=50, required=True, label='Дата выполнения')
    status = forms.ChoiceField(required=True, choices=StatusChoice.choices, label='статус')
