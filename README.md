python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
 
python manage.py loaddata reviews.json

python manage.py loaddata services.json
