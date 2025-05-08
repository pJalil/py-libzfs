"""

 * py-libzfs
 * Copyright (C) 2025 Jalil HESSANE

 * Permission is hereby granted, free of charge, to any person obtaining a copy of
 * this software and associated documentation files (the "Software"), to deal in
 * the Software without restriction, including without limitation the rights to
 * use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
 * the Software, and to permit persons to whom the Software is furnished to do so,
 * subject to the following conditions:

 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.

 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
 * SOFTWARE.

"""

import ctypes

py_libzfs = ctypes.CDLL("/usr/lib/py-libzfs/py-libzfs.so")

# Snapshot creation
py_libzfs.create_snapshot.argtypes = [ctypes.c_char_p, ctypes.c_bool]
py_libzfs.create_snapshot.restype = ctypes.c_int

# Snapshot destruction
py_libzfs.destroy_snapshot.argtype = ctypes.c_char_p
py_libzfs.destroy_snapshot.restype = ctypes.c_int

class Snapshots:
    def __init__(self, name):
        self.name = name

    def create(snapshot: str, recursive: bool = False) -> int:
        return py_libzfs.create_snapshot(snapshot.encode(), recursive)

    def destroy(snapshot: str) -> int:
        return py_libzfs.destroy_snapshot(snapshot.encode())
        
    def __repr__(self):
        return f"<Snapshots '{self.name}'>"
