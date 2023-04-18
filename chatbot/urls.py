from django.urls import path, include
from .views import chat, storyline_view

urlpatterns = [
    path('chatbot/', chat, name='chat'),
    path('storyline/', storyline_view, name='storyline_view'),
]