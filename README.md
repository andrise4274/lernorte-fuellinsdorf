# Capstone

The purpose of this Website called Lernorte is to have a location to collect and manage all good places of learning in nature arround and for this school. This should support teachers to go outside with their students, in an age of more and more digital dependency. It is currently running on [https://lernorte-fuellinsdorf.vercel.app](https://lernorte-fuellinsdorf.vercel.app). The teachers should be able to enter new places, without any programming knowledge.

## Distinctiveness

The distinctivness comes through the usage of kml files and iframes from swisstopo [https://map.geo.admin.ch](https://map.geo.admin.ch). Each time something in the Media Model is changed via the admin panel, a global kml file compiled out of the database automatically. On an overwiew map, each place of learning is displayed with symbols and by clicking on it, the user is directly brought to the corresponding route.

## Complexity
Each time something in the Media Model is changed via the admin panel, a global kml file compiled out of the database automatically, which speeds up the process of adding a new place of learning massively. A receiver on post_save, triggers the update_kml_file() function which tries to recompile a new kml file in a temporary file. If this process is successfull the temporary file is saved as the updated file. If not, the old file is kept. On the fronend JavaScript is used to make all tables searchable and to sort all tables. 

The other parts of the webpage are not to complex and the use of the admin Panel for the teachers (with help of a detailed guide), omits the necessity of any Django forms and custom user authentication.

## Django backend
In addition to views.py, models.py, urls.py and admin.py I used an apps.py and a signals.py to handle the compilation of the global kml file.

### signals.py and apps.py
The apps.py configures signals.py. Signals.py is responsible to write the new global kml file for the overwiev map out of the data in Model Lernort.

## Frontend
The webpage has 3 main pages unde the routes:
- / -> main page of the website
- /map -> overview map
- /table -> detailed table with each category for each learning place

The user can search and sort each table with help of javascript. Intentionally slightly hidden is the guidance to enter a new learning place via the admin route, which is linked on there. To use the admin page, user credentials are necessary.
- /anleitung -> guide with all necessary Information
- /admin -> used by the teachers to add a new learning place


## Deployment
I used vercel to deploy the app, since the traffic is low and it is necessary keep it free.
### Database
The real application runs on a Postgress db with the code uncommented in settings.py. This Code uses the default Django sqlite db.

### Media and static Files
Static files are stored under static/lernorte. There is the table.js file which handles all frontend searching and sorting tasks and the global stylesheet. Further the icons and pictures for the guidance are stored in their respective folders.

The media files are stored under uploads/lernorte/media. There the global kml file and the lernort kml files and pictures are stored. To serve the static and mediafiles the urls are added to url-patterns and Debug = True, which is not ideal but it works in this special case.


Since it is not possible to edit the global kml file and upload pictures on vercel in an easy way (without costs), the Lernorte Model is split into a Lernorte Model (which is updated by the teachers) and a Media Model which has to be maintained by the administrator. To upload pictures and kml files and recompile the global kml file, the admin has to run the applications localy and the push the updated files to github, from where vercel makes a new build. Until now, I haven't found a better solution. But still, most of the work can be done by the teachers on their own.


### vercel.json
This file is for the deployment of a django application to vercel.


## run the application

To run the application locally, just run

``python manage.py makemigrations lernorte``

``python manage.py migrate``

``python manage.py collectstatic``

``python manage.py runserver``