from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
# from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
    AuthenticationForm, 
    UserCreationForm, 
    PasswordChangeForm,
)
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_http_methods, require_POST
from django.shortcuts import render, redirect
from .forms import CustomUserChangeForm



# 로그인
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('employee:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'employee:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


# 로그아웃
@login_required
@require_POST
def logout(request):
    if request.user.is_authenticated:
        user_logout(request)
    return redirect('employee:index')


# 회원가입
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('employee:index')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_vaild():
            
            form.save()
    else:
        form = UserCreationForm()

    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)


# 회원탈퇴
@login_required
@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        user_logout(request)
    return redirect('employee:index')


# 회원정보수정
@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    form = CustomUserChangeForm()
    if request.method == 'POST':
            form = CustomUserChangeForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form' : form
    }
    return render(request, 'accounts/update.html', context)


# 비밀번호변경
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')

    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form
    }
    return render(request, 'accounts/change_password.html', context)