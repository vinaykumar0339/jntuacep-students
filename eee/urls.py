from django.urls import path
from .views import eee,eeeRegulation,eeeYear,eeeSemester

urlpatterns = [
    path('',eee,name="eee"),
    path('<str:regulation>/',eeeRegulation,name='eee-regulation'),
    path('<str:regulation>/<int:year>/',eeeYear,name='eee-year'),
    path('<str:regulation>/<int:year>/<int:semester>',eeeSemester,name='eee-semester'),
]