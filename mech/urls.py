from django.urls import path
from .views import mech,mechRegulation,mechYear,mechSemester

urlpatterns = [
    path('',mech,name='mech'),
    path('<str:regulation>/',mechRegulation,name='mech-regulation'),
    path('<str:regulation>/<int:year>/',mechYear,name='mech-year'),
    path('<str:regulation>/<int:year>/<int:semester>',mechSemester,name='mech-semester'),
]