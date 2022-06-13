from django.contrib import admin
from .models import Complain, ComplainComment


# Register your models here.
class ComplainAdmin(admin.ModelAdmin):
    pass

admin.site.register(Complain, ComplainAdmin)
admin.site.register(ComplainComment)