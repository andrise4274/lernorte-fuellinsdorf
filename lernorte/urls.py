from django.urls import path
from . import views

urlpatterns = [
		path("",views.index, name="index"),
        path("lernort/<str:lernort>", views.lernort, name="lernort"),
        path("karte", views.karte, name="karte"),
        path("tabelle", views.tabelle, name="tabelle"),
        path("anleitung", views.anleitung, name="anleitung"),
        path("error", views.error, name="error")
]


