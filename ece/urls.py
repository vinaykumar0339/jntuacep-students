from django.urls import path
from .views import ece,eceRegulation,eceYear,eceSemester

urlpatterns = [
    path('',ece,name='ece'),
    path('<str:regulation>/',eceRegulation,name='ece-regulation'),
    path('<str:regulation>/<int:year>/',eceYear,name='ece-year'),
    path('<str:regulation>/<int:year>/<int:semester>',eceSemester,name='ece-semester'),
]