/*
 * This file and its contents are supplied under the terms of the
 * Common Development and Distribution License ("CDDL"), version 1.0.
 * You may only use this file in accordance with the terms of version
 * 1.0 of the CDDL.
 *
 * A full copy of the text of the CDDL should have accompanied this
 * source.  A copy of the CDDL is also available via the Internet at
 * http://www.illumos.org/license/CDDL.
 */

/*
 * Copyright 2025 Jalil HESSANE <jalil.hessane@proton.me>
 */

#include <libzfs.h>
#include <stdio.h>
#include <string.h>


/*
 * Dataset management. Maybe going to add more props in the future.
 * Return positive value for external (ZFS) errors, negative for internal errors.
 * 
 * dataset is the complete name of the dataset, including pool, parent datasets, etc.
 * ex: rpool/data/test
 */

int create_dataset(const char *dataset, const char *mountpoint, const char *compression) {
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

    	if (nvlist_add_string(props, "mountpoint", mountpoint) != 0 ||
        	nvlist_add_string(props, "compression", compression) != 0) {
        	nvlist_free(props);
        	libzfs_fini(g_zfs);
        	return -3;
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
