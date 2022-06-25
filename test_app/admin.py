from django.contrib import admin

# Register your models here.
from django.contrib import admin

from test_app.models import Task

admin.site.register(Task)

