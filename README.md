# Build
To build the C interface and copy the Python code to your ```site-package``` directory, run:
```bash
make install
```

To make only symbolic links (usefull for developement), run:
```bash
make dev
```

To clean, run:
```bash
make clean
```

To uninstall, run:
```bash
make uninstall
```

*Because of the installation paths (/usr/lib/python3.12/site-packages for python files and /usr/lib/py-libzfs for the C interface), you should be using pfexec or sudo, or set permissions to write and read from theses directory for your current user.*

Tested on OmniOS r151052, built with GCC 14 and using Python 3.12.
