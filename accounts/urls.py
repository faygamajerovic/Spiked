from django.urls import path
from. import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('dashboard/favorites', views.favorite_list, name='favorite_list'),
    path('fav/<int:id>/', views.favorite_add, name='favorite_add')
]