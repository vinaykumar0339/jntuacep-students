from django.urls import path
from .views import civil, civilRegulation, civilYear, civilSemester

urlpatterns = [
    path('',civil,name='civil'),
    path('<str:regulation>/',civilRegulation,name='civil-regulation'),
    path('<str:regulation>/<int:year>/',civilYear,name='civil-year'),
    path('<str:regulation>/<int:year>/<int:semester>',civilSemester,name='civil-semester'),
]