run:
	python manage.py runserver localhost:8000

make:
	python manage.py makemigrations

migrate:
	python manage.py migrate

freeze:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt

test:
	python manage.py test

drop:
	dropdb devs-talk

create:
	createdb devs-talk

live:
	python manage.py livereload

set:
	export PGUSER=postgres

activate:
	source virtual/Scripts/activate

admin:
	python manage.py createsuperuser --username admin --email admin@admin.com

hadmin:
	heroku run python manage.py createsuperuser --username admin --email admin@admin.com

hmake:
	heroku run python manage.py makemigrations

hmigrate:
	heroku run python manage.py migrate

pushdb:
	heroku pg:push api DATABASE_URL

reset:
	heroku pg:reset DATABASE

addon:
	heroku addons:create heroku-postgresql:hobby-dev
