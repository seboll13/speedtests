#include <time.h>
#include <stdio.h>
#include <stdlib.h>

int *insertion_sort(int *arr, int n) {
    int i, j, key;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
    return arr;
}

void _wait(int n) {
    for (; n > 0; n--);
}

int main(int argc, char *argv[]) {
    srand(time(NULL));
    if (argc == 2) {
        int SIZE = atoi(argv[1]);
        int *arr = malloc(SIZE * sizeof(int));
        for (int i = 0; i < SIZE; i++) {
            arr[i] = rand() % 1000;
        }
        //_wait(SIZE);
        clock_t start = clock();
        insertion_sort(arr, SIZE);
        clock_t end = clock();
        printf("Time taken: %f seconds.\n", (double)(end - start) / CLOCKS_PER_SEC);
        return 0;
    }
    printf("Usage: ./speed <size of array>\n");
    return 1;
}