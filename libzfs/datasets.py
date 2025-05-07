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

py_libzfs.create_dataset.argtypes = [
        ctypes.c_char_p, 
        ctypes.POINTER(ctypes.c_char_p), 
        ctypes.POINTER(ctypes.c_char_p), 
        ctypes.c_int
 ]
py_libzfs.create_dataset.restype = ctypes.c_int

py_libzfs.destroy_dataset.argtype = ctypes.c_char_p
py_libzfs.destroy_dataset.restype = ctypes.c_int

py_libzfs.edit_dataset.argtypes = [
        ctypes.c_char_p, 
        ctypes.POINTER(ctypes.c_char_p), 
        ctypes.POINTER(ctypes.c_char_p), 
        ctypes.c_int
 ]
py_libzfs.edit_dataset.restype = ctypes.c_int

py_libzfs.get_all_datasets.restype = ctypes.POINTER(ctypes.c_char_p)

py_libzfs.get_children_datasets.argtype = ctypes.c_char_p
py_libzfs.get_children_datasets.restype = ctypes.POINTER(ctypes.c_char_p)


class Datasets:
    def __init__(self, name):
        self.name = name

    def create(dataset: str, props: dict) -> int:
        count = len(props)

        keys_list = [key.encode("utf-8") for key in props.keys()]
        values_list = [value.encode("utf-8") for value in props.values()]

        keys_array = (ctypes.c_char_p * count)(*keys_list)
        values_array = (ctypes.c_char_p * count)(*values_list)
    
        result = py_libzfs.create_dataset(
            dataset.encode("utf-8"),
            keys_array,
            values_array,
            count
        )

        return result

    def edit(dataset: str, props: dict) -> int:
        count = len(props)

        keys_list = [key.encode("utf-8") for key in props.keys()]
        values_list = [value.encode("utf-8") for value in props.values()]

        keys_array = (ctypes.c_char_p * count)(*keys_list)
        values_array = (ctypes.c_char_p * count)(*values_list)
    
        result = py_libzfs.edit_dataset(
            dataset.encode("utf-8"),
            keys_array,
            values_array,
            count
        )

        return result

    def get_all() -> list:
        ptr = py_libzfs.get_all_datasets()
        result = []
        i = 0
        while ptr[i]:
            result.append(ptr[i].decode())
            i += 1
        return result

    def get_children(dataset) -> list:
        ptr = py_libzfs.get_children_datasets(dataset.encode())
        result = []
        i = 0
        while ptr[i]:
            result.append(ptr[i].decode())
            i += 1
        return result

    # If used with True, it will destroy all children datasets. Use at your own risk
    def destroy(dataset: str, force=False) -> int:
        if force==False:
            result = py_libzfs.destroy_dataset(dataset.encode())
        elif force==True:
            children = Datasets.get_children(dataset)
            for i in range(len(children)-1,-1,-1):
                py_libzfs.destroy_dataset(children[i].encode())
            result = py_libzfs.destroy_dataset(dataset.encode())
        else:
            result=-10

        return result

    def __repr__(self):
        return f"<Dataset '{self.name}'>"
