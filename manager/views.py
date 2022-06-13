from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth import get_user_model

from .models import AttendanceList
from .forms import AttendanceListForm


@login_required
def index(request, username):
    attendanceLists = AttendanceList.objects.order_by('-pk')
    User = get_user_model()
    person = get_object_or_404(User, username=username)
    context = {
        'person': person,
        'attendanceLists': attendanceLists,
    }
    return render(request, 'manager/index.html', context)

@login_required
def scanner(requset, username):
    return render(requset, 'manager/scanner.html')

@login_required
@require_http_methods(['GET', 'POST'])
def create(request, username):
    if request.method == 'POST':
        form = AttendanceListForm(request.POST)
        print(form)
        if form.is_valid():
            print(1)
            attendance = form.save(commit=False)
            attendance.user = request.user
            attendance.save()
            print(attendance)
            print(2)
            return redirect('manager:index', username)
    else:
        form = AttendanceListForm()
    context = {
        'form': form,
    }
    print(3)
    return render(request, 'manager/scanner.html', context)




# import cv2
# import pyzbar.pyzbar as pyzbar
# import pygame


# Create your views here.
# @login_required
# def index(request, username):
#     # scanner에 DB로 저장한 user의 pk를 가지고 불러오기
#     User = get_user_model()
#     person = get_object_or_404(User, username=username)
#     context = {
#         'person': person,
#     }
#     return render(request, 'manager/index.html', context)


# def scanner(request):
#     return render(request, 'manager/scanner.html')

# def scanner(request, username):
#     name_list = []

#     cap = cv2.VideoCapture(0)
#     # pygame.mixer.init()
#     # pygame.mixer.music.load('qrbarcode_beep.wav')

#     while id is None:
#         success, frame = cap.read()

#         if success:
#             for code in pyzbar.decode(frame):
#                 my_code = code.data.decode('utf-8')     # 저장할 데이터 (인식된 데이터) -> 고유값 + 이름

#                 if my_code not in name_list:
#                     print("인식 성공 : ", my_code)
#                     name_list.append(my_code)           # name_list에 read 값 저장 (중복 방지)
#                     # pygame.mixer.music.play()           # 음악 실행

#                 else:
#                     print("이미 등록되었습니다")

#             cv2.imshow('QRcode Barcode Scan', frame)    # 웹에서도 프로그램으로 뜨나?

#             # key = cv2.waitKey(1)                        # ESC 누르면 종료
#             # if key == 27:
#             #     break
#             if id is not None:
#                 cv2.destroyAllWindows()

#     cap.release()
#     cv2.destroyAllWindows()

#     # user = 관리자 /
#     AttendanceList.objects.create(user=username ,employee={username : name_list})
#     return
