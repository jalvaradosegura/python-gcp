.DEFAULT_GOAL = help

help:
	@echo "Use this project as explained in the following"
	@echo ""
	@echo "build"
	@echo "	Build containers for the API and the MySQL database. It also install new packages"
	@echo "up"
	@echo "	Execute docker-compose up -d"
	@echo "down"
	@echo "	Shut down the containers"
	@echo "test"
	@echo "	Run the tests for this project"
	@echo "logs"
	@echo "	Print the logs of the containers"
build:
	docker-compose up -d --build
up:
	docker-compose up -d
down:
	docker-compose down
test:
	docker-compose exec web python manage.py test
logs:
	docker-compose logs
