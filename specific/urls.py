from specific.views import *
from django.urls import path 

app_name = 'specific'

urlpatterns=[
    path('specific1/',specific1,name='specific1'),
    path('specific2/',specific2,name='specific2'),
]