CC = gcc
CFLAGS = -Wall -Wextra -g
PYTHON = python3
MOJO = mojo
NODE = node
CARGO = cargo
RUST_PATH = rust_simulator/

all: simulator cargo_build

run: all python mojo node simulator_execute cargo_execute

python:
	$(PYTHON) simulator.py

mojo:
	$(MOJO) simulator.mojo

node:
	$(NODE) simulator.js

# C build and execution
simulator: simulator.o
	$(CC) $(CFLAGS) -o $@ $^

simulator.o: simulator.c
	$(CC) $(CFLAGS) -c $<

simulator_execute:
	./simulator

# Rust build and execution
cargo_build:
	cd $(RUST_PATH) && $(CARGO) build --release

cargo_execute:
	cd $(RUST_PATH) && $(CARGO) run --release

# Cleanup build artifacts
clean:
	rm -f *.o simulator
	cd $(RUST_PATH) && $(CARGO) clean
	clear

.PHONY: all clean
