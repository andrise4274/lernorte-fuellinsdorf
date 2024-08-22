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
    try:
        if lernort.media:  # Check if media exists
            url1 = lernort.media.bild1.url
            url2 = lernort.media.bild2.url
            url3 = lernort.media.bild3.url
            url_kml = lernort.media.kml_file.url
    except:
        url1 = ""
        url2 = ""
        url3 = ""
        url_kml = ""
    

    # render lernort.html with all data
    return render(request, "lernorte/lernort.html", {
        "lernort": lernort,
        "url1": url1,
        "url2": url2,
        "url3": url3,
        "url_kml": url_kml
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

