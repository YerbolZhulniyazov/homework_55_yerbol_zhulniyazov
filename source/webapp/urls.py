from django.urls import path

from webapp.views.tasks import add_view, detail_view, update_view, delete_view, confirm_delete
from webapp.views.base import index_view

urlpatterns =[
    path("", index_view, name='index'),
    path("task/", index_view),
    path('task/add', add_view, name='add_task'),
    path('task/<int:pk>', detail_view, name='detail_task'),
    path('task/<int:pk>/update/', update_view, name='task_update'),
    path('task/<int:pk>/delete/', delete_view, name='task_delete'),
    path('task/<int:pk>/confirm_delete/', confirm_delete, name='confirm_delete')
]
