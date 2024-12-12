from django.urls import path
from . import views


urlpatterns = [
    path('bot-users/', views.bot_users_view, name='bot_users'),
    path('bot-users/<int:pk>/', views.bot_user_detail_view, name='bot_user_detail'),
    path('words/', views.word_view, name='words'),
    path('words/<int:pk>/', views.word_detail_view, name='word_detail'),
]