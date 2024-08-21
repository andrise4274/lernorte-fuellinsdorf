# make migrations
python3.12 manage.py makemigrations lernorte
python3.12 manage.py migrate 
python3.12 manage.py collectstatic
