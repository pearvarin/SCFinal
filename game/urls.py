"""URL's for the chat app."""

from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    # path('chats/', views.ChatSessionView.as_view()),
    # path('chats/<uri>/', views.ChatSessionView.as_view()),
    # path('chats/<uri>/messages/', views.ChatSessionMessageView.as_view()),
    path('game/', views.GameSessionView.as_view()),
    path('game/<uri>/', views.GameSessionView.as_view()),
    path('game/<uri>/submissions/', views.GameSessionMessageView.as_view()),
    #path('',TemplateView.as_view(template_name='index.html'))
]

