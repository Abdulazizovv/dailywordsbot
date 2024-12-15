from django.urls import path
from . import views


urlpatterns = [
    path('bot-users/', views.bot_users_view, name='bot_users'),
    path('bot-users/<int:pk>/', views.bot_user_detail_view, name='bot_user_detail'),
    path('words/', views.word_view, name='words'),
    path('words/<int:pk>/', views.word_detail_view, name='word_detail'),
    path('categories/', views.category_view, name='categories'),
    path('categories/<int:pk>/', views.category_detail_view, name='category_detail'),
    path('categories/user/<int:user_id>/', views.user_category_view, name='user_categories'),
    path('categories/public/', views.public_category_view, name='public_categories'),
    path('categories/private/<int:user_id>/', views.private_user_category_view, name='private_user_categories'),
]