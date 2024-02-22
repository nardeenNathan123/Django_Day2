from django.contrib import admin

from company.models import Employee, Team

# Register your models here.

admin.site.register(Team)
admin.site.register(Employee)

