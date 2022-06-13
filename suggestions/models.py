from django.db import models
from django.conf import settings

# Create your models here.
# pk name title content image
class Suggestion(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    STATUS_CHOICES = (
        ('1', '처리중'),
        ('2', '반려'),
        ('3', '처리완료'),
    )
    suggestion = models.OneToOneField(Suggestion, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    reason = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status
