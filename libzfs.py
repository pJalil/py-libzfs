"""

 * pylibzfs
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

ilibzfs = ctypes.CDLL("./ilibzfs.so")  # change according to path

# dataset creation
ilibzfs.create_dataset.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
ilibzfs.create_dataset.restype = ctypes.c_int

def create_dataset(dataset, mountpoint, compression):
    result = ilibzfs.create_dataset(
        dataset.encode(),
        mountpoint.encode(),
        compression.encode()
    )
    if result == 0:
        return "success"
    else:
        return f"Error code: {result}"

#dataset destruction
ilibzfs.destroy_dataset.argtype = ctypes.c_char_p
ilibzfs.destroy_dataset.restype = ctypes.c_int

def destroy_dataset(dataset):
    result = ilibzfs.destroy_dataset(dataset.encode())
    
    if result == 0:
        return "success"
    else:
        return f"Error code: {result}"

ilibzfs.get_all_datasets.restype = ctypes.POINTER(ctypes.c_char_p)

def get_all_datasets():
    ptr = ilibzfs.get_all_datasets()
    result = []
    i = 0
    while ptr[i]:
        result.append(ptr[i].decode())
        i += 1
    return result

ilibzfs.get_children_datasets.argtype = ctypes.c_char_p
ilibzfs.get_children_datasets.restype = ctypes.POINTER(ctypes.c_char_p)

def get_children_datasets(dataset):
    ptr = ilibzfs.get_children_datasets(dataset.encode())
    result = []
    i = 0
    while ptr[i]:
        result.append(ptr[i].decode())
        i += 1
    return result

# Test
if __name__ == "__main__":
    print(create_dataset("rpool/mydata", "/data/mydata", "lz4"))
    print(create_dataset("rpool/mydata/datamy", "/data/mydata/datamy", "lz4"))
    print(get_all_datasets())
    print(get_children_datasets("rpool/mydata"))
    print(destroy_dataset("rpool/mydata/datamy"))
    print(destroy_dataset("rpool/mydata"))

