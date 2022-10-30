from django.urls import path
from . import views

app_name= 'python'
urlpatterns=[
    path('css/', views.css, name= 'css'),
    path('html/', views.html, name='html'),
]