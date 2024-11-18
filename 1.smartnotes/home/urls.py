from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.LoginInterfaceView.as_view(), name='login'),  # Ensure trailing slash
    path('logout/', views.LogoutInterfaceView.as_view(), name='logout'),  # Ensure trailing slash
    path('signup/', views.SignUpView.as_view(), name='signup'),  # Corrected URL and view name
]
