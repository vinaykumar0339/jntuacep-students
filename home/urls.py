from django.urls import path
from .views import home,signup,signin,logout,contactUs,results,profile

urlpatterns = [
    path('',home,name="home"),
    path('signup',signup,name='signup'),
    path('signin',signin,name='signin'),
    path('logout',logout,name='logout'),
    path('contactus',contactUs,name='contactus'),
    path('results',results,name='results'),
    path('profile',profile,name='profile')
]