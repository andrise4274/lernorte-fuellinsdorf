import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Lernort


import tempfile
import shutil


def get_kml_section(lernort):
    lernort_link = f"https://lernorte-fuellinsdorf.vercel.app/lernort/{lernort.name}"

    icons = ""
    if lernort.wald:
        icons += '<img src="https://andrise4274.github.io/fuellinsdorf-umgebung/static/icons/environment.png" width="100px"/><br>\n'
    if lernort.feuerstelle:
        icons += '<img src="https://andrise4274.github.io/fuellinsdorf-umgebung/static/icons/bonfire_2436266.png" width="100px"/><br>\n'
    if lernort.feuerholz:
        icons += '<img src="https://andrise4274.github.io/fuellinsdorf-umgebung/static/icons/campfire_6199010.png" width="100px"/><br>\n'
    if lernort.trinkwasser:
        icons += '<img src="https://andrise4274.github.io/fuellinsdorf-umgebung/static/icons/tap-water.png" width="100px"/><br>\n'
    if lernort.bademoeglichkeit:
        icons += '<img src="https://andrise4274.github.io/fuellinsdorf-umgebung/static/icons/swimming.png" width="100px"/><br>\n'
    if lernort.unterstand:
        icons += '<img src="https://andrise4274.github.io/fuellinsdorf-umgebung/static/icons/roof.png" width="100px"/><br>\n'
    if lernort.abfall:
        icons += '<img src="https://andrise4274.github.io/fuellinsdorf-umgebung/static/icons/recycle-bin.png" width="100px"/><br>\n'
    


    kml_section = f"""<Placemark>
                <name>	{lernort.name}	</name>
                <description><![CDATA[ 
                    <a style="display: inline-block;				
                    text-decoration: none;				
                    color: black;				
                    background-color: rgb(18, 164, 217) !important;				
                    border-radius: 4px;				
                    padding: 5px 10px;				
                    margin: 10px;				
                    font-weight: bold;				
                    font-size: 18px;				
                    target="_blank" href="{lernort_link}">{lernort.name}
                        </a>
                        
                    <br>
                    <img src="https://andrise4274.github.io/fuellinsdorf-umgebung/static/icons/task_11319878.png" width="100px"/><b>{lernort.wegzeit} min</b>
                    <br>
                    {icons}		
                ]]>				
				</description>								
                <Style><IconStyle><scale>1.125</scale><Icon><href>https://map.geo.admin.ch/api/icons/sets/default/icons/001-marker@1x-255,0,0.png</href><gx:w>48</gx:w><gx:h>48</gx:h></Icon><hotSpot x="24" y="6" xunits="pixels" yunits="pixels"/></IconStyle><LabelStyle><color>ff0000ff</color><scale>1.5</scale></LabelStyle></Style>
                <ExtendedData><Data name="textOffset"><value>0,-44.75</value></Data><Data name="type"><value>marker</value></Data></ExtendedData>
                <Point><coordinates>{lernort.coordinate_E},{lernort.coordinate_N}</coordinates></Point>
            </Placemark>\n"""
    return kml_section

def compile_global_kml(file):
    for lernort in Lernort.objects.all():
        section = get_kml_section(lernort)
        file.write(section)
    file.write('</Document></kml>')

@receiver(post_save, sender=Lernort)
def update_static_file(sender, instance, **kwargs):
    print("trying to update and recompile global.kml...")
    file_path = os.path.join(settings.BASE_DIR, 'uploads', 'lernorte', 'global.kml')

    try:
        with tempfile.NamedTemporaryFile('w', delete=False, dir=os.path.dirname(file_path)) as tmp_file:
            tmp_file.write('<?xml version="1.0" encoding="UTF-8"?><kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom"><Document>\n')

            # Write KML content
            compile_global_kml(tmp_file)

        # Replace the original file with the temporary file
        shutil.move(tmp_file.name, file_path)
        print("success")

    except Exception as e:
        # Log the error and keep the old version of the file
        if os.path.exists(tmp_file.name):
            os.remove(tmp_file.name)  # Clean up the temp file

        print(f"error: {e}")