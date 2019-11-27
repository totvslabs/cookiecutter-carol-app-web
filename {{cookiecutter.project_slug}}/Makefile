ifeq ($(OS),Windows_NT)
	OPEN := start
else
	UNAME := $(shell uname -s)
	ifeq ($(UNAME),Linux)
		OPEN := xdg-open
	endif
	ifeq ($(UNAME),Darwin)
		OPEN := open
	endif
endif

.PHONY: help

help: ## Show this help message
	@echo "{{cookiecutter.project_slug}} Makefile help.\n"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

