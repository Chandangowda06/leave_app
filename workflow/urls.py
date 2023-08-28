from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('profile/apply-for-leave', views.apply, name='profile/apply-leave'),
    path('update-profile/', views.update, name='update-profile'),
    path('profile/leave-requests', views.leave_requests, name='profile/leave-requests'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]