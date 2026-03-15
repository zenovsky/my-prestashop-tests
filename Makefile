.PHONY: up-infra setup test clean run-all

ADMIN_EMAIL ?= example@example.com
ADMIN_PASSWORD ?= example

up-infra:
	docker-compose up -d db phpmyadmin prestashop

setup: up-infra
	chmod +x setup/*.sh
	setup/wait_for_prestashop.sh
	setup/setup_api_key.sh

test: setup
	docker-compose run --rm -e ADMIN_EMAIL=$(ADMIN_EMAIL) -e ADMIN_PASSWORD='$(ADMIN_PASSWORD)' tests 

clean:
	docker-compose down -v
	rm -f .env

run-all: clean
	@$(MAKE) test; \
	STATUS=$$?; \
	$(MAKE) clean; \
	exit $$STATUS