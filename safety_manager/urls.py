from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('employee/', include('employee.urls')),
    path('manager/', include('manager.urls')),
    path('accounts/', include('accounts.urls')),
    path('suggestions/', include('suggestions.urls')),
    path('complain/', include('complain.urls'))
]