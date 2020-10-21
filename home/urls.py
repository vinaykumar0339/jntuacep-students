from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import home,signup,signin,logout,contactUs,results,profile,pdfUpload
urlpatterns = [
    path('',home,name="home"),
    path('signup',signup,name='signup'),
    path('signin',signin,name='signin'),
    path('logout',logout,name='logout'),
    path('contactus',contactUs,name='contactus'),
    path('results',results,name='results'),
    path('profile',profile,name='profile'),
    path('pdf-uploads',pdfUpload,name='pdf-uploads'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

