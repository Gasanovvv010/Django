from django.urls import path
from . import views

urlpatterns = [
    path('fibonacci/', views.fibonacci_view, name='fibonacci'),
]
