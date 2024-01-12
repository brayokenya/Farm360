# Makefile for Django Application

# Virtual environment setup
venv:
	python3 -m venv venv

# Install dependencies
install:
	pip install -r requirements.txt

# Run development server
run:
	python manage.py runserver

# Run migrations
migrate:
	python manage.py migrate

# Create a superuser
createsuperuser:
	python manage.py createsuperuser

# Collect static files
collectstatic:
	python manage.py collectstatic

# Clean pycache and temporary files
clean:
	find . -name "*.pyc" -exec rm -f {} \;
	find . -name "__pycache__" -exec rm -rf {} \;
	rm -rf venv

# Help message
help:
	@echo "Available targets:"
	@echo "  make venv            - Create a virtual environment"
	@echo "  make install         - Install dependencies"
	@echo "  make run             - Run development server"
	@echo "  make migrate         - Run database migrations"
	@echo "  make createsuperuser - Create a superuser"
	@echo "  make collectstatic   - Collect static files"
	@echo "  make clean           - Clean up pycache and temporary files"
	@echo "  make help            - Display this help message"

.PHONY: venv install run migrate createsuperuser collectstatic clean help
