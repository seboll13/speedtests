CC = gcc
CFLAGS = -Wall -Wextra -g
PYTHON = python
MOJO = mojo
NODE = node

all: simulator

execute: simulator
	./simulator
	$(PYTHON) simulator.py
	$(MOJO) simulator.mojo
	$(NODE) simulator.js

python:
	$(PYTHON) simulator.py

mojo:
	$(MOJO) simulator.mojo

node:
	$(NODE) simulator.js

simulator: simulator.o
	$(CC) $(CFLAGS) -o simulator simulator.o

simulator.o: simulator.c
	$(CC) $(CFLAGS) -c simulator.c

clean:
	rm -f *.o simulator
	clear

.PHONY: all clean
