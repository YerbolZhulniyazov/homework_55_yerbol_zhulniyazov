from django.db import models
from django.db.models import TextChoices
from django.utils import timezone


class StatusChoice(TextChoices):
    NEW = 'NEW', 'Новая'
    IN_PROGRESS = 'IN_PROGRESS', 'В прогрессе'
    COMPLETED = 'COMPLETED', 'Выполнена'


# Create your models here.

class TODO(models.Model):
    status = models.CharField(verbose_name='Статус', choices=StatusChoice.choices, max_length=20,
                              default=StatusChoice.NEW)
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Заголовок", default="null")
    description = models.CharField(max_length=100, null=False, blank=False, verbose_name="Описание",
                                   default="null")
    detailed_description = models.TextField(max_length=2500, null=False, blank=False,
                                            verbose_name="Подробное описание", default="null")
    completion_date = models.DateField(default="", verbose_name="Дата выполнения")
    is_deleted = models.BooleanField(verbose_name='удалено', null=False, default=False)
    deleted_at = models.DateTimeField(verbose_name='Дата и время удаления', null=True, default=None)

    def __str__(self):
        return f"{self.title} - {self.status}"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
