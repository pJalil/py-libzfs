CC = gcc
CFLAGS = -Wall -fPIC
LDFLAGS = -shared -lzfs

SRC = py-libzfs.c
TARGET = py-libzfs.so

all: $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $(TARGET) $(SRC) $(LDFLAGS)

install: $(TARGET)
	mkdir -p $(PREFIX)/lib
	cp $(TARGET) $(PREFIX)/lib/

clean:
	rm -f $(TARGET)

