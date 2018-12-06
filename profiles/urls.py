from django.urls import path

from . import views
urlpatterns = [
    path('upload/', views.upload, name="upload" ),
    path('', views.index, name="index" ),
    path('login/', views.login, name="loguj" ),
]
