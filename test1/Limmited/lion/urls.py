from typing import ValuesView
from django.urls import path
from . import views

app_name= 'lion'
urlpatterns=[
    path('review/', views.review, name='review'),
    path('thanks/',views.thanks, name= 'thanks')
]

