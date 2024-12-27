from django.urls import path
from app1.views import *

app_name='app1'


urlpatterns = [
    
    path('Home/',Home,name='Home'),
    path('Matches/',Matches,name='Matches'),
    path('Teams/',Teams,name='Teams'),
    path('Stats/',Stats,name='Stats'),
    path('point_table/',point_table,name='point_table')
    
]