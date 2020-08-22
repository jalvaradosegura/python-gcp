.DEFAULT_GOAL = help

help:
	@echo "Use this project as explained in the following"
	@echo ""
	@echo "make test"
	@echo "	Run the tests for this project"
test:
	docker-compose exec web python manage.py test