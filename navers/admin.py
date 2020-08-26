from django.contrib import admin
from .models import Naver


@admin.register(Naver)
class NaverAdmin(admin.ModelAdmin):
    list_display = ['name', 'admission_date', 'job_role', 'user']
    list_filter = ['name', 'birthdate', 'admission_date', 'job_role', 'user']
    search_fields = ['admission_date', 'job_role', 'user']
