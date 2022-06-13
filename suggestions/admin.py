from django.contrib import admin
from .models import Suggestion, Comment


# Register your models here.
class SuggestionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Suggestion, SuggestionAdmin)
admin.site.register(Comment)