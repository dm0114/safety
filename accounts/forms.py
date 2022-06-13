from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model


# 수정 필요
class CustomUserChangeForm(UserChangeForm):

    password = None

    class Meta:
        model = get_user_model() # User
        fields = ('email', 'first_name', 'last_name',)


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['date_of_birth'].required = True
        self.fields['phone_number'].required = True
        self.fields['user_type'].required = True
        
        self.fields['name'].widget.attrs['placeholder'] = "홍길동"
        self.fields['date_of_birth'].widget.attrs['placeholder'] = "1960-01-01"
        self.fields['phone_number'].widget.attrs['placeholder'] = "01011112222"
        self.fields['username'].widget.attrs['placeholder'] = "아이디 기입"
        self.fields['password1'].widget.attrs['placeholder'] = "비밀번호"
        self.fields['password2'].widget.attrs['placeholder'] = "비밀번호 확인"

    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ['name', 'date_of_birth', 'phone_number', 'username', 'user_type']
