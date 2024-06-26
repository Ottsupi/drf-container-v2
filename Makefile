# Define variables
MANAGE = python manage.py

# Define targets and recipes
.PHONY: run migrate superuser app shell


run:
	gunicorn -c ./gunicorn/gunicorn.local.py core.wsgi:application --reload

prod:
	gunicorn -c ./gunicorn/gunicorn.production.py core.wsgi:application

migrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

superuser:
	$(MANAGE) createsuperuser

app:
	@read -p "Enter the app name: " app_name; \
	mkdir -p apps/$$app_name; \
	$(MANAGE) startapp $$app_name apps/$$app_name; \
	echo "Don't forget to edit the name in $$app_name/apps.py config"

shell:
	$(MANAGE) shell_plus --ipython

urls:
	$(MANAGE) show_urls
