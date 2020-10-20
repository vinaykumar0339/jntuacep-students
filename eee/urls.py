from django.urls import path
from .views import eee

urlpatterns = [
    path('',eee,name="eee")
]