# app-api
# Dockerizing Django REST framework

#To run this app
#Build images
docker-compose build 
#Start containers
docker-compose up

#Create SQL migration files
docker-compose run app python3 /app/manage.py makemigrations

#Apply migration models
docker-compose run app python3 /app/manage.py migrate

#Create superuser
docker-compose run app python3 /app/manage.py createsuperuser

#Create new module
docker-compose run app python3 /app/manage.py startapp [APP_NAME]
