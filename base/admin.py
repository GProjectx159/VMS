from django.contrib import admin

from .models import User, Department, Vacation, DepartmentManager


admin.site.register(User)
admin.site.register(Department)
admin.site.register(Vacation)
admin.site.register(DepartmentManager)