from django.urls import path
from . import views


app_name = 'employee'
urlpatterns = [
    path('', views.index, name='index'),
    path('study/', views.study, name='study'),          # 메인 스터디 페이지
    path('<int:pk>/', views.lecture, name='lecture'),   # 특정 강의
    path('<int:pk>/test/', views.test, name='test'),    # 특정 강의에 대한 테스트
    path('<username>/', views.suggestion, name= 'suggestion'),   # 안전관리 제언
]
