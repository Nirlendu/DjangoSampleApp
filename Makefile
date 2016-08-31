make:
	sudo pip install enum
	python manage.py sqlall sites
	python manage.py syncdb
	python manage.py runserver
