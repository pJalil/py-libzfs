PREFIX = /usr/lib/py-libzfs

PYTHON_SITE = /usr/lib/python3.12/site-packages
install:
	cd src && $(MAKE) install PREFIX=$(PREFIX)
	mkdir -p $(PYTHON_SITE)/libzfs
	cp -r libzfs/* $(PYTHON_SITE)/libzfs/

dev:
	cd src && $(MAKE)
	mkdir -p $(PREFIX)
	ln -sf `pwd`/src/py-libzfs.so $(PREFIX)/py-libzfs.so
	mkdir -p $(PYTHON_SITE)
	ln -sfn `pwd`/libzfs $(PYTHON_SITE)/libzfs

uninstall:
	rm -f $(PREFIX)/py-libzfs.so
	rm -rf $(PYTHON_SITE)/libzfs

clean:
	cd src && $(MAKE) clean

