from django.contrib import admin
from .models import AttendanceList


# Register your models here.
class AttendanceListAdmin(admin.ModelAdmin):
    pass

admin.site.register(AttendanceList, AttendanceListAdmin)