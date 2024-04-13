CC = gcc
CFLAGS = -Wall -Wextra -g
PYTHON = python3
MOJO = mojo
NODE = node
CARGO = cargo
RUST_PATH = rust_simulator/
C_DIR = c_simulator

all: build run

build: c_build cargo_build

run: python mojo node c_execute cargo_execute

python:
	$(PYTHON) simulator.py

mojo:
	$(MOJO) simulator.mojo

node:
	$(NODE) simulator.js

# C build and execution
c_build: $(C_DIR)/simulator

$(C_DIR)/simulator: simulator.o
	$(CC) $(CFLAGS) -o $@ $^

simulator.o: $(C_DIR)/simulator.c
	$(CC) $(CFLAGS) -c $<

c_execute:
	./$(C_DIR)/simulator

# Rust build and execution
cargo_build:
	cd $(RUST_PATH) && $(CARGO) build --release

cargo_execute:
	cd $(RUST_PATH) && $(CARGO) run --release

# Cleanup build artifacts
clean:
	rm -rf *.o c_build
	cd $(RUST_PATH) && $(CARGO) clean
	clear

.PHONY: all clean
