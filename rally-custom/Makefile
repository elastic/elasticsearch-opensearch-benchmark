TAG := ${image}

all: build pull

build:
	@echo "\n::: Building and pushing multi-arch image $(TAG)"
	docker buildx build --push -f Dockerfile --platform linux/amd64,linux/arm64/v8 --tag $(TAG) .

pull:
	docker pull $(TAG)
