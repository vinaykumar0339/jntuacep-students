from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
import matplotlib as mp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('civil/',include('civil.urls')),
    path('eee/',include('eee.urls')),
    path('mech/',include('mech.urls')),
    path('ece/',include('ece.urls')),
    path('cse/',include('cse.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

