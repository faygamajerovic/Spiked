from django.urls import path
from. import views

urlpatterns = [
    path('', views.home, name='home'),
    path('spirits', views.spirits, name='spirits'),
    path('glasses', views.glasses, name='glasses'),
]