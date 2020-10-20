from django.urls import path
from .views import ece

urlpatterns = [
    path('',ece,name='ece')
]