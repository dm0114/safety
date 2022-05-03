from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.shortcuts import render, redirect
from employee.models import StudyList

# Create your views here.
# 작업자들이 들어가면 보게 될 메인 화면
@login_required
def index(request):
    return render(request, 'employee/index.html')

# 모든 강의 목록, 최신 순으로 나열
@login_required
def study(request):
    lectures = StudyList.objects.order_by('-pk')
    context = {
        'lectures': lectures,
    }
    return render(request, 'employee/study.html', context)

# 강의 - 글이나 영상을 미리 DB에 넣어놔야 가져올 것 같은데??
@login_required
def lecture(request, pk):
    lecture = get_object_or_404(StudyList, pk=pk)
    context = {
        'lecture': lecture,
    }
    return render(request, 'employee/lecture.html', context)

# 시험 - 시험 페이지는 HTML로 작성되어야 할 것 같은데...??
@login_required
def test(request, pk):
    return render(request, 'employee/test.html')

# 입출결 - QR코드 생성
@login_required
def attendance(request):
    return
