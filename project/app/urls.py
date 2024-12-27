from django.urls import path
from app.views import *

app_name='app'


urlpatterns = [
    path('RCB/',RCB,name='RCB'),
    path('CSK/',CSK,name='CSK'),
    path('MI/',MI,name='MI'),
    path('KKR/',KKR,name='KKR'),
    path('LSG/',LSG,name='LSG'),
    path('RR/',RR,name='RR'),
    path('DC/',DC,name='DC'),
    path('SRH/',SRH,name='SRH'),
    path('GT/',GT,name='GT'),
    path('PBKS/',PBKS,name='PBKS'),
    
    
]