from django.urls import path
from . import views

urlpatterns = [
    path('about', views.about, name='about'),
    path('health', views.health_check, name='health_check'),
    path('api/messages', views.message_api, name='message_api'),
]
