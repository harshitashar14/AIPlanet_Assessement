Install requirements.
```
pip install -r requirements.txt
```
Add .env file in the same folder as settings.py and database details and django secret key in .env file
```
DATABASE_NAME=assessment_db
DATABASE_USER=root
DATABASE_PASSWORD=database_password
DATABASE_HOST=127.0.0.1
DATABASE_PORT=3306
SECRET_KEY=This_is_a_Demo_Secret_key
```
Create assessment_db database in Mysql.

```
CREATE DATABASE assessment_db;
```
Make migrations ,migrate and then run the server
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
