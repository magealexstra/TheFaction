from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('projects/', views.ProjectListView.as_view(), name='project_list'),
    path('admin-login/', views.AdminLoginView.as_view(), name='admin_login'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('info/', views.InfoResourceListView.as_view(), name='info_list'),
]