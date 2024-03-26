from django.urls import path

from . import views

urlpatterns = [
    path('django/', views.django_index),
    path('drf/', views.DRFIndex.as_view()),
    path('user/', views.HelloUserView.as_view()),
    path('', views.HelloListView.as_view()),
]
