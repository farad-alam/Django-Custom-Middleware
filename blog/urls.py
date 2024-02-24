from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('excep/', views.exception_view, name='excep'),
]
