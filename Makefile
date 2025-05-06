# py-libzfs
# Copyright (C) 2025 Jalil HESSANE
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
# SOFTWARE.


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

