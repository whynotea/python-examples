.PHONY: default
default: all

.PHONY: all
all: conda-create
	@$(MAKE) conda-run

.PHONY: conda-run
conda-run:
	conda run --no-capture-output -p .conda python ./maze.py maze1.txt

.PHONY: conda-create
conda-create: .conda

.conda:
	@echo "Building conda environment"
	conda env create -p .conda -f ./environment.yml

.PHONY: conda-update
conda-update:
	conda env update -p .conda -f ./environment.yml

