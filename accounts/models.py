from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


# Create your models here.
class User(AbstractUser):
    TYPE_CHOICES = (
        ('1', '근로자/장비운전자/유도자'),
        ('2', '작업지휘자'),
        ('3', '관리감독자'),
        ('4', '감독원/건설사업관리자'),
    )

    name = models.CharField("성명", max_length=20)
    date_of_birth = models.DateField("생년월일", max_length=8)
    phone_number = models.CharField("전화번호", validators=[RegexValidator(r'010-?[1-9]\d{3}-?\d{4}$')], max_length=13, blank=True)
    user_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    
    REQUIRED_FIELDS = ['name', 'date_of_birth', 'phone_number', 'user_type']
