.PHONY: default
default: all

.PHONY: all
all:
	build

.PHONY: build
build:
	podman build -t buildoze:latest -f ./build/buildozer/Containerfile ./build/buildozer
	podman run --rm -it -v $$(pwd)/.buildozer:/root/.gradle -v $$(pwd)/.buildozer:/root/.buildozer -v $$(pwd):/workspace -w /workspace buildoze:latest /bin/bash -c "buildozer -v android debug"

.PHONY: conda-run
conda-run:
	conda run -p .conda python ./kvcalc/main.py

.PHONY: conda-create
conda-create:
	conda env create -p .conda -f ./environment.yml

.PHONY: conda-update
conda-update:
	conda env update -p .conda -f ./environment.yml
