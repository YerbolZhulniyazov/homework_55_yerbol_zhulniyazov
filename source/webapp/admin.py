from django.contrib import admin

from webapp.models import TODO


# Register your models here.
class TODOAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'detailed_description', 'status', 'completion_date',
                    'is_deleted', 'deleted_at')
    list_filter = ('id', 'title', 'description', 'status', 'completion_date',
                   'is_deleted', 'deleted_at')
    search_fields = ('title', 'status', 'is_deleted', 'deleted_at')
    fields = ('title', 'description', 'detailed_description', 'status', 'completion_date', 'is_deleted', 'deleted_at')
    readonly_fields = ('id',)


admin.site.register(TODO, TODOAdmin)
