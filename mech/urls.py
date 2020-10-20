from django.urls import path
from .views import mech,R_15,R_19,R_15_firstyear

urlpatterns = [
    path('',mech,name='mech'),
    path('R-15/',R_15,name='mech-R-15'),
    path('R-19/',R_19,name='mech-R-15'),
    path('R-15/<int:year>/',R_15_firstyear,name='mech-R-15-1'),
]