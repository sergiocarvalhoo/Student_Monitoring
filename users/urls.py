from django.urls import path

from .views import (
    register,
    do_login,
    do_logout,
)

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', do_login, name='login'),
    path('logout/', do_logout, name='logout'),
]
