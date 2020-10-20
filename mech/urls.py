from django.urls import path
from .views import mech,R_15,R_19

urlpatterns = [
    path('',mech,name='mech'),
    path('R-15',R_15,name='mech-R-15'),
    path('R-19',R_19,name='mech-R-15'),
]