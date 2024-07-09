# include .env

TAG_LINT := webapp-lint
TAG_LINT_TESTS := webapp-lint-tests
TAG_TESTS := webapp-tests
TAG_WEBAPP_PROD := webapp-allainclair-prod

docker-lint-build:
	docker build \
		--tag=$(TAG_LINT) \
		--target=lint-run .

docker-lint-run: docker-lint-build
	docker run --name $(TAG_LINT) --rm $(TAG_LINT)

docker-lint-tests-build:
	docker build \
		--tag=$(TAG_LINT_TESTS) \
		--target=lint-tests-run .

docker-lint-tests-run: docker-lint-tests-build
	docker run --name $(TAG_LINT_TESTS) --rm $(TAG_LINT_TESTS)

docker-tests-build:
	docker build \
		--tag=$(TAG_TESTS) \
		--target=tests-run .

docker-tests-run: docker-tests-build
	docker run --name $(TAG_TESTS) --rm $(TAG_TESTS)

docker-prod-build:
	docker build \
		--tag=$(TAG_WEBAPP_PROD) \
		--target=prod .

docker-prod-run: docker-prod-build
	docker stop $(TAG_WEBAPP_PROD) || true
	docker rm $(TAG_WEBAPP_PROD) || true
	docker run --name $(TAG_WEBAPP_PROD) \
		--rm --detach  -p 8001:8001 \
		-v ${DATA_DIR_HOST_PROD}:${DATA_DIR_DOCKER} \
		$(TAG_WEBAPP_PROD)
