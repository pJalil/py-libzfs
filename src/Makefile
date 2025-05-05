CC = gcc
CFLAGS = -Wall -fPIC -I.
LDFLAGS = -shared -lzfs

SRC = py-libzfs.c datasets.c
OBJ = $(SRC:.c=.o)
TARGET = py-libzfs.so

all: $(TARGET)

$(TARGET): $(OBJ)
	$(CC) -o $@ $(OBJ) $(LDFLAGS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

install: $(TARGET)
	mkdir -p $(PREFIX)/lib
	cp $(TARGET) $(PREFIX)/lib/

clean:
	rm -f $(OBJ) $(TARGET)

