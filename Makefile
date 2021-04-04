build-dev:
	make stop-dev
	docker-compose -f build/development/docker-compose.yml up -d --build
run-dev:
	docker-compose -f build/development/docker-compose.yml up -d --build
stop-dev:
	docker-compose -f build/development/docker-compose.yml down -v
logs-dev:
	docker-compose -f build/development/docker-compose.yml logs -f