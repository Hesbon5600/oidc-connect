#!/bin/bash

#@-- help command to show usage of make commands --@#

SHELL := /bin/bash
SHELLFLAGS := -c
activate := env/bin/activate
help:
	@echo "----------------------------------------------------------------------------"
	@echo "-                     Available commands                                   -"
	@echo "----------------------------------------------------------------------------"
	@echo "---> make env              - To create virtual environment"
	@echo "---> make install          - To install dependencies from poetry.lock"
	@echo "---> make migrate          - To update the database with the latest migration"
	@echo "---> make run              - To start the server"
	@echo "---> make help             - To show usage commands"
	@echo "----------------------------------------------------------------------------"



env:
	@ echo '<<<<<<<<<<Creating virtual environment>>>>>>>>>'
	python3.10 -m venv env
	@ echo ''


install:
	@ echo '<<<<<<<<<<installing requirements>>>>>>>>>'
	poetry install
	@ echo ''

migrate:
	@ echo '<<<<<<<<<<creating migrations>>>>>>>>>'
	python manage.py migrate
	@ echo ''

run:
	@ echo '<<<<<<<<<<starting server>>>>>>>>>'
	python manage.py runserver 8080
	@ echo ''

default: help