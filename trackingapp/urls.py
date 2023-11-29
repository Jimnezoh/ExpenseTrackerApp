from django.urls import path
from trackingapp import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('addexpense/', views.addexpense, name='addexpense'),
    path('manage/', views.manage, name='manage'),
    path('addbudget/', views.addbudget, name='addbudget'),
    path('edit/<pk>/', views.Edit, name='edit'),
    path('delete/<pk>/', views.Delete, name='delete'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('editbudget/<pk>/', views.Editbudget, name='editbudget'),
    path('deletebudget/<pk>/', views.Deletebudget, name='deletebudget'),
]
