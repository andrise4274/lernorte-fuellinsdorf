from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Lernort



def index(request):
    # get all name and wegzeiten of lernorte from db
    lernorte = Lernort.objects.values('name', 'wegzeit')

    return render(request, "lernorte/index.html", {
        "lernorte": lernorte
    })


def lernort(request, lernort):
    # check if lernort exists
    try:
        lernort = Lernort.objects.get(name=lernort)
    except:
        return render(request, "lernorte/error.html", {
        "msg": f"kein Lernort {lernort} gefunden"
    })
    # render lernort.html with all data
    return render(request, "lernorte/lernort.html", {
        "lernort": lernort
    })


def karte(request):
    # get global.kml url
    url = ""
    # render map.html
    return render(request, "lernorte/map.html", {
        "url": url
    })


def tabelle(request):
    # get all lernorte from db
    lernorte = Lernort.objects.all()
    # render 
    return render(request, "lernorte/table.html", {
        "lernorte": lernorte
    })


def anleitung(request):
    return render(request, "lernorte/anleitung.html")


def error(request):
    return render(request, "lernorte/error.html", {
        "msg": f"kein Lernort {lernort} gefunden"
    })

