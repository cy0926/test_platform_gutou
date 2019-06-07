from django.contrib import admin
from user_app.models import Project
from user_app.models import Module


# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'describe', 'status', 'create_time', 'update_time']
    search_fields = ['name']
    list_filter = ['status']


class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'describe', 'create_time']
    search_fields = ['name']
    list_filter = ['name']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Module, ModuleAdmin)
