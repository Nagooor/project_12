from specific.views import *
from django.urls import path
app_name='specific'
urlpatterns=[
    path('pspk/',pspk,name='pspk'),
    path('rc/',rc,name='rc'),
]