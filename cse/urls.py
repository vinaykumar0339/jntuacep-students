from django.urls import path
from .views import cse
urlpatterns = [
    path('',cse,name='cse')
]