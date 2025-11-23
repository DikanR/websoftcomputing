from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tugas3/", views.tugas3, name="tugas3"),
    path("tugas4/", views.tugas4, name="tugas4"),
]