from django.urls import path
from .views import civil

urlpatterns = [
    path('',civil,name='civil')
]