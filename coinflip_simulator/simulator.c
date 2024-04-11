#include <time.h>
#include <stdlib.h>
#include <stdio.h>

#define PROB 0.4

/**
 * Simulates a biased coin flip where it lands on tails w.p. PROB
 * 
 * @return 1 if the coin lands on heads, 0 if it lands on tails
*/
int flip_biased_coin() {
    return (float)rand() / (float)RAND_MAX >= PROB;
}

/**
 * Uses the Von Neumann method to generate an unbiased run of coin flips.
 * The function loops over a pair of biased coin flips until both flips are different.
 * 
 * @return the result of the second flip
*/
int get_unbiased_run() {
    while (1) {
        int first = flip_biased_coin();
        int second = flip_biased_coin();
        if (first != second)
            return second;
    }
}

/**
 * Generates an unbiased sequence of coin flips and counts the number of heads.
 * 
 * @param length the length of the sequence
 * @return the number of heads in the sequence
*/
int generate_unbiased_sequence(int length) {
    int count = 0;
    for (int i = 0; i < length; i++) {
        count += get_unbiased_run();
    }
    return count;
}

/**
 * Main function
*/
int main() {
    srand(time(NULL));
    int length = 1e6;
    int start = clock();
    int total_heads = generate_unbiased_sequence(length);
    int end = clock();
    printf("Number of heads: %d\n", total_heads);
    printf("C Time: %f [s]\n", (double)(end - start) / CLOCKS_PER_SEC);
}