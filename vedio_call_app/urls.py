from django.urls import path
from .views import register_view, index, login_view, dashboard, vediocall, logout_view, join_room
urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('meeting/', vediocall, name='meeting'),
    path('logout/', logout_view, name='logout'),
    path('join/', join_room, name='join_room'),
    path('', index, name='index'),
]
