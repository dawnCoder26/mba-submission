
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users.views import LoginUser, Dashboard, Applications, ApplicationDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mbasubmission.urls')),
    
    path('login/', LoginUser, name='login-user'),
    path('dashboard/', Dashboard, name='dashboard'),
    path('dashboard/applications/', Applications, name='applications'),
    path('dashboard/applications/235532/', ApplicationDetail, name='application-detail'),
]

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)