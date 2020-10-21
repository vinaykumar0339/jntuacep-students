from django.urls import path
from .views import cse,display
urlpatterns = [
    path('',cse,name='cse'),
    path('Data/',display,name='data')
]