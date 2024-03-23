from django.urls import path
from . import views

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("animale/", views.AnimaleListView.as_view(), name="animale"),
    path("<int:animale_id>", views.animale_detalii, name="animale_detalii")
]
app_name = "animale"