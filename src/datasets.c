/*
 * pylibzfs
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
#include "datasets.h"

/*
 * Dataset management. Maybe going to add more props in the future.
 * Return positive value for external (ZFS) errors, negative for internal errors.
 * 
 * dataset is the complete name of the dataset, including pool, parent datasets, etc.
 * ex: rpool/data/test
 */

static char *dataset_list[MAX_DATASETS];
static int dataset_count = 0;

//Maybe should add some kind of verification for keys and values
int create_dataset(const char *dataset, const char **keys, const char **values, int count) {
	libzfs_handle_t *g_zfs; 
        nvlist_t *props;

        g_zfs = libzfs_init();
        if (!g_zfs) {
        	return -1;
	}	

        if (nvlist_alloc(&props, NV_UNIQUE_NAME, 0) != 0) {
        	libzfs_fini(g_zfs);
        	return -2;
    	}

    	for (int i = 0; i < count; ++i) {
        	if (keys[i] && values[i]) {
            		if (nvlist_add_string(props, keys[i], values[i]) != 0) {
                		nvlist_free(props);
                		libzfs_fini(g_zfs);
                		return -3;
            		}
        	}
   	}

    	int ret = zfs_create(g_zfs, dataset, ZFS_TYPE_FILESYSTEM, props);

    	nvlist_free(props);
    	libzfs_fini(g_zfs);

    	return ret;
}

int destroy_dataset(const char *dataset) {
	libzfs_handle_t *g_zfs;
	zfs_handle_t *zhp;

	g_zfs = libzfs_init();
	if (!g_zfs){
		return -1;
	}

	zhp = zfs_open(g_zfs, dataset, ZFS_TYPE_DATASET);
	if (!zhp) {
		libzfs_fini(g_zfs);
		return -4;
	}

	int ret = zfs_destroy(zhp, B_FALSE);
	if (ret !=0) {
		zfs_close(zhp);
		libzfs_fini(g_zfs);
		return ret;
	}

	zfs_close(zhp);
	libzfs_fini(g_zfs);

	return 0;
}

// callback function internal to ilibzfs
int collect_dataset(zfs_handle_t *zhp, void *unused) {
    	if (dataset_count >= MAX_DATASETS) {
        	zfs_close(zhp);
        	return -5; 
    	}

    	const char *name = zfs_get_name(zhp);
    	dataset_list[dataset_count] = strdup(name);
    	dataset_count++;

    	zfs_iter_filesystems(zhp, collect_dataset, NULL);
    	zfs_close(zhp);
    	return 0;
}


char **get_all_datasets() {
    	libzfs_handle_t *g_zfs = libzfs_init();
    	if (!g_zfs) return NULL;

    	dataset_count = 0;
    	memset(dataset_list, 0, sizeof(dataset_list));

    	zfs_iter_root(g_zfs, collect_dataset, NULL);

    	libzfs_fini(g_zfs);
    	return dataset_list;
}

char **get_children_datasets(const char *dataset) {
    	libzfs_handle_t *g_zfs = libzfs_init();
    	if (!g_zfs) return NULL;

	zfs_handle_t *zhp;

	zhp = zfs_open(g_zfs, dataset, ZFS_TYPE_DATASET);
	if (!zhp) {
		libzfs_fini(g_zfs);
		return NULL;
	}

    	dataset_count = 0;
    	memset(dataset_list, 0, sizeof(dataset_list));

    	zfs_iter_filesystems(zhp, collect_dataset, NULL);

    	libzfs_fini(g_zfs);
    	return dataset_list;
}
