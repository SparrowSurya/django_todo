from django.contrib import admin

from .models import Task

admin.site.site_header = 'Task App'

admin.site.register(Task)
