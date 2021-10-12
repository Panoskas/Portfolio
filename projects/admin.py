from django.contrib import admin
from projects.models import Project

class Projectadmin (admin.ModelAdmin):
    pass


admin.site.register (Project, Projectadmin)
