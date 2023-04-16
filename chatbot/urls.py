from django.urls import path, include
from .views import chat

urlpatterns = [
    path('chatbot/', chat, name='chat'),
]