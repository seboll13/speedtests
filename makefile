CC = gcc
CFLAGS = -Wall -Wextra -g
PYTHON = python
NODE = node

all: speed

execute: speed
	./speed 10000
	$(PYTHON) speed.py 10000
	$(NODE) speed.js 10000

python:
	$(PYTHON) speed.py 10000

javascript:
	$(NODE) speed.js 10000

speed: speed.o
	$(CC) $(CFLAGS) -o speed speed.o

speed.o: speed.c
	$(CC) $(CFLAGS) -c speed.c

clean:
	rm -f *.o speed
	clear

.PHONY: all clean
