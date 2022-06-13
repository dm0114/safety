from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('employee/', include('employee.urls')),
    path('manager/', include('manager.urls')),
    path('accounts/', include('accounts.urls')),
    path('suggestions/', include('suggestions.urls')),
    path('complain/', include('complain.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)