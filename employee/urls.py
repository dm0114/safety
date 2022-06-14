from django.urls import path
from . import views


app_name = 'employee'
urlpatterns = [
    path('', views.index, name='index'),
    path('login_index/', views.login_index, name='login_index'),
    path('quiz/', views.quiz, name='quiz'),
    path('study/', views.study, name='study'),          # 메인 스터디 페이지
    path('<int:pk>/', views.lecture, name='lecture'),   # 특정 강의
    path('<int:pk>/test/', views.test, name='test'),    # 특정 강의에 대한 테스트
    path('<username>/', views.suggestion, name= 'suggestion'),   # 안전관리 제언
]
