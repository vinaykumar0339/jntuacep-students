from django.urls import path

from .views import cse,display
urlpatterns = [
    path('',cse,name='cse'),
    path('Data/',display,name='data')
]
from .views import cse,cseRegulation,cseYear,cseSemester
urlpatterns = [
    path('',cse,name='cse'),
    path('<str:regulation>/',cseRegulation,name='cse-regulation'),
    path('<str:regulation>/<int:year>/',cseYear,name='cse-year'),
    path('<str:regulation>/<int:year>/<int:semester>',cseSemester,name='cse-semester'),

]