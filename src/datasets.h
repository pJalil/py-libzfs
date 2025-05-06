#ifndef DATASET_H
#define DATASET_H

//In theory the limit should be arround 2^64, adapt to your needs.
#define MAX_DATASETS 1024  

int create_dataset(const char *dataset, const char **keys, const char **values, int count);
int destroy_dataset(const char *dataset);
int edit_dataset(const char *dataset, const char **keys, const char **values, int count);
char **get_all_datasets(void);
char **get_children_datasets(const char *dataset);

#endif // DATASET_H
