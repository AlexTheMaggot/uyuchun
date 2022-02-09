# Imports
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
# End Imports


# Config
urlpatterns = [
    path('admin/', include('admin.urls', namespace='admin')),
    path('', include('mainapp.urls', namespace='mainapp')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# End Config
