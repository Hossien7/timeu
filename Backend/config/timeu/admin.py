from django.contrib import admin
from . import models


@admin.register(models.Timeu)
class TodoAdmin(admin.ModelAdmin):
    pass

