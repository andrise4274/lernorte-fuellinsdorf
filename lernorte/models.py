from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Lernort(models.Model):
    name = models.CharField(max_length=100, unique=True)
    coordinate_N = models.DecimalField(max_digits=9, decimal_places=6)
    coordinate_E = models.DecimalField(max_digits=9, decimal_places=6)
    wegzeit = models.IntegerField(verbose_name="Wegzeit in Minuten", help_text="Die geschätzte Wegzeit in Minuten")

    wald = models.BooleanField(null=True, blank=True)
    feuerstelle = models.BooleanField(null=True, blank=True)
    feuerholz = models.BooleanField(null=True, blank=True)
    trinkwasser = models.BooleanField(null=True, blank=True)
    bademoeglichkeit = models.BooleanField(null=True, blank=True)
    unterstand = models.BooleanField(null=True, blank=True)
    abfall = models.BooleanField(null=True, blank=True)

    waldtext = models.CharField(max_length=250)
    feuerstelletext = models.CharField(max_length=250)
    feuerholztext = models.CharField(max_length=250)
    trinkwassertext = models.CharField(max_length=250)
    bademoeglichkeittext = models.CharField(max_length=250)
    unterstandtext = models.CharField(max_length=250)
    abfalltext = models.CharField(max_length=250)

    text = models.TextField(max_length=2500)
    wegbeschreibung = models.TextField(max_length=2500)


class Media(models.Model):
    lernort = models.OneToOneField(Lernort, on_delete=models.CASCADE, related_name="media")
    bild1 = models.ImageField(upload_to="lernorte/pictures")
    bild2 = models.ImageField(upload_to="lernorte/pictures")
    bild3 = models.ImageField(upload_to="lernorte/pictures")

    kml_file = models.FileField(upload_to="lernorte/kml_files")