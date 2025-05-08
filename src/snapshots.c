/*
 * py-libzfs
 * Copyright (C) 2025 Jalil HESSANE
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
 * SOFTWARE.
 */

#include <libzfs.h>
#include <stdio.h>
#include <string.h>

int create_snapshot(const char *snapshot, boolean_t recursive) {
	libzfs_handle_t *g_zfs = libzfs_init();
	
	int ret =zfs_snapshot(g_zfs, snapshot, recursive, NULL);
	libzfs_fini(g_zfs);
	
	return ret;
}

int destroy_snapshot(const char *snapshot) {
	libzfs_handle_t *g_zfs = libzfs_init();
	if (!g_zfs)
	return -1;

	char snapshot_buf[1024];
    	strncpy(snapshot_buf, snapshot, sizeof(snapshot_buf));
	snapshot_buf[sizeof(snapshot_buf) - 1] = '\0';

	char *at = strchr(snapshot_buf, '@');
		if (!at) {
	        libzfs_fini(g_zfs);
	        return -11;
        }

	*at = '\0';
        const char *dataset = snapshot_buf;
	const char *snapname = at + 1;

	zfs_handle_t *zhp = zfs_open(g_zfs, dataset, ZFS_TYPE_DATASET);
	if (!zhp) {
	        libzfs_fini(g_zfs);
	        return -3;
	}

	int ret = zfs_destroy_snaps(zhp, (char *)snapname, B_FALSE);
	zfs_close(zhp);
	libzfs_fini(g_zfs);

	return ret;
}
