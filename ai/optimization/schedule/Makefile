.PHONY: default
default: all

.PHONY: all
all: conda-create
	@$(MAKE) conda-run

.PHONY: conda-run
conda-run:
	conda run --no-capture-output -p .conda python ./schedule1.py

.PHONY: conda-run-%
conda-run-%:
	conda run --no-capture-output -p .conda python $*.py

.PHONY: conda-create
conda-create: .conda

.conda:
	@echo "Building conda environment"
	conda env create -p .conda -f ./environment.yml

.PHONY: conda-update
conda-update:
	conda env update -p .conda -f ./environment.yml

