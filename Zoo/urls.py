from django.urls import path

from Zoo import views

urlpatterns = [
    path('', views.animal_list, name = 'animal_list'),
    path('new/', views.animal_create, name='animal_add'),
    path('update/<int:id>/', views.animal_update, name = 'animal_update'),
    path('delete/<int:id>/', views.animal_delete, name = 'animal_delete'),
    path('login/', views.user_login, name='login'),
    path('create_user/', views.create_user, name='create_user'),
]