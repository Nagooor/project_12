from generic.views import *
from django.urls import path
app_name='nagoor'
urlpatterns=[
    path('ssmb/',ssmb,name='ssmb'),
    path('ntr/',ntr,name='ntr'),
]