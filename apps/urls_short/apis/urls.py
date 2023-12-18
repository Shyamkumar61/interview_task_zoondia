from django.urls import path
from .views import UrlDetailView, UrlView, AccessShorUrlView

urlpatterns = [
    path('url-list/', UrlView.as_view()),
    path('url-details/<int:pk>/', UrlDetailView.as_view()),
    path('<str:token>/', AccessShorUrlView.as_view()),
]