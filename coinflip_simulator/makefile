PYTHON = python3
MOJO = mojo
NODE = node
JAVA = java
JAVAC = javac
JAVA_SRC = java_simulator
JAVA_MAIN = coinflip_simulator.java_simulator.Main
CARGO = cargo
RUST_PATH = rust_simulator/
CC = gcc
CFLAGS = -Wall -Wextra -g
C_DIR = c_simulator

all: build run

build: c_build cargo_build

run: python mojo node java gcc rust

python:
	$(PYTHON) simulator.py

mojo:
	$(MOJO) simulator.mojo

node:
	$(NODE) simulator.js

# Java build and execution
java: java_compile java_execute

java_compile:
	$(JAVAC) -d . $(JAVA_SRC)/*.java

java_execute:
	$(JAVA) -cp . $(JAVA_MAIN)

# C build and execution
gcc: c_build c_execute

c_build: $(C_DIR)/simulator

$(C_DIR)/simulator: simulator.o
	$(CC) $(CFLAGS) -o $@ $^

simulator.o: $(C_DIR)/simulator.c
	$(CC) $(CFLAGS) -c $<

c_execute:
	./$(C_DIR)/simulator

# Rust build and execution
rust: cargo_build cargo_execute

cargo_build:
	cd $(RUST_PATH) && $(CARGO) build --release

cargo_execute:
	cd $(RUST_PATH) && $(CARGO) run --release

# Cleanup build artifacts
clean:
	find . \( -name "*.class" -o -name "*.o" \) -type f -delete
	cd $(C_DIR) && rm -f simulator
	cd $(RUST_PATH) && $(CARGO) clean
	clear

.PHONY: all clean
