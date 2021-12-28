from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_mainpage, name="MainPage"),
    path("<str:Choose>/", views.Analyze.as_view(), name="Analyze"),
]