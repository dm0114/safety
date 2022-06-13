from django.db import models
from django.conf import settings

# Create your models here.
class AttendanceList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    employee = models.CharField("근로자", max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
