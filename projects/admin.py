from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']
    list_filter = ['name', 'user']
    search_fields = ['name', 'user']
