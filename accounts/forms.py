from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model


# 수정 필요
class CustomUserChangeForm(UserChangeForm):

    password = None

    class Meta:
        model = get_user_model() # User
        fields = ('email', 'first_name', 'last_name',)
