"""

 * This file and its contents are supplied under the terms of the 
 * Common Development and Distribution License ("CDDL"), version 1.0.
 * You may only use this file in accordance with the terms of version 
 * 1.0 of the CDDL. 
 * 
 * A full copy of the text of the CDDL should have accompanied this
 * source.  A copy of the CDDL is also available via the Internet at
 * http://www.illumos.org/license/CDDL."""

""" 

 * Copyright 2025 Jalil HESSANE <jalil.hessane@proton.me>

"""

import ctypes

clibzfs = ctypes.CDLL("./libzfs.so")  # change according to path

clibzfs.create_dataset.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
clibzfs.create_dataset.restype = ctypes.c_int

clibzfs.destroy_dataset.argtype = ctypes.c_char_p
clibzfs.destroy_dataset.restype = ctypes.c_int

def create_dataset(dataset, mountpoint, compression):
    result = clibzfs.create_dataset(
        dataset.encode(),
        mountpoint.encode(),
        compression.encode()
    )
    if result == 0:
        return "success"
    else:
        return f"Error code: {result}"

def destroy_dataset(dataset):
    result = clibzfs.destroy_dataset(dataset.encode())
    
    if result == 0:
        return "success"
    else:
        return f"Error code: {result}"

# Test
if __name__ == "__main__":
    print(create_dataset("rpool/mydata", "/data/mydata", "lz4"))
    print(destroy_dataset("rpool/mydata"))

