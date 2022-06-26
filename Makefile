.PHONY: install start lint-poetry lint-black lint-isort lint format-black format-isort format

BYellow=\033[1;33m
Color_Off=\033[0m
CmdIcon=➡️

define cmd
	@echo "${CmdIcon}  ${BYellow}$(1)${Color_Off}"
	@eval $(1)
endef

install:
	$(call cmd,poetry install)

start:
	$(call cmd,poetry run start)

lint-poetry:
	$(call cmd,poetry check -n)

lint-black:
	$(call cmd,poetry run black --check --diff .)

lint-isort:
	$(call cmd,poetry run isort --check --diff .)

lint: lint-poetry lint-black lint-isort

format-black:
	$(call cmd,poetry run black .)

format-isort:
	$(call cmd,poetry run isort .)

format: format-black format-isort