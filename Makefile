migrate:
	docker-compose exec web python manage.py makemigrations
	docker-compose exec web python manage.py migrate

create_user:
	docker-compose exec web python manage.py createsuperuser


build:
	docker-compose build db
	docker-compose build web

build-db:
	docker-compose build db

build-web:
	docker-compose build web

up:
	docker-compose up -d db
	sleep 2
	docker-compose up web

stop:
	docker-compose stop web
	docker-compose stop db

test:
	docker-compose exec web python manage.py test