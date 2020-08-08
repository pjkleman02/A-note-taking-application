from django.contrib import admin
from django.urls import path
from .views import PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('', views.home, name='notepad'),
    path('notepad/new/', PostCreateView.as_view(), name='notepad-create'),
    path('notepad/<int:pk>/update/', PostUpdateView.as_view(), name='notepad-update'),
    path('notepad/<int:pk>/delete/', PostDeleteView.as_view(), name='notepad-delete'),
]
