"""URL's for the chat app."""

from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView
from rest_framework import routers
from .viewsets import *

from . import views
router = routers.DefaultRouter()
router.register(r'User',UserViewSet)


urlpatterns = [
    path('game/', views.GameSessionView.as_view()),
    path('game/<uri>/', views.GameSessionView.as_view()),
    path('game/<uri>/submissions/', views.GameSessionMessageView.as_view()),
    path('game/<uri>/gamemanager/'),
    path('game/<uri>/gamemanager/<period>/'),
    path('game/<uri>/<user>/'),
    path('game/<uri>/<user>/<period>/'),
    path('login/', TemplateView.as_view(template_name="login.html")),
    path('game/<uri>/<user>/graph/'),
    path('game/<uri>/<user>/<user>/forecast/'), #supplier/buyer
    path('game/<uri>/<user>/<user>/dedicated_inventory/'),
    path('game/<uri>/<user>/financials/'),
    path('game/<uri>/<user>/parameters/'),
    path('game/<uri>/<user>/comments/'),
    path('game/<uri>/<user>/forecast_history/'),
    path('game/<uri>/gamemanager/'),
    path('game/<uri>/settings/'),
    router.urls

    # path('',TemplateView.as_view(template_name='index.html'))
]

