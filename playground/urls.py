from django.urls import path
from . import views

app_name = 'playground'
# URLConf
urlpatterns = [
    path('hello/', views.say_hello),
    #path('hello/<name>/', views.say_hello, name='Aishak'),
    
]