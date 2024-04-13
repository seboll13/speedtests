#include <time.h>
#include <stdlib.h>
#include <stdio.h>

#define PROB 0.4

// Struct to store the result of an experiment
typedef struct ExperimentResult {
    int heads;
    float time;
} ExperimentResult;

/**
 * @brief Simulates a biased coin flip where it lands on tails w.p. PROB
 * 
 * @return 1 if the coin lands on heads, 0 if it lands on tails
*/
int flip_biased_coin() {
    return (float)rand() / (float)RAND_MAX >= PROB;
}

/**
 * @brief Uses the Von Neumann method to generate an unbiased run of coin flips.
 * The function loops over a pair of biased coin flips until both flips are different.
 * 
 * @return 0 if the run is HT, 1 if the run is TH.
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
 * @brief Generates an unbiased sequence of coin flips and counts the number of heads.
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
 * @brief Runs the unbiased sequence generation experiment a given # of times.
 * 
 * @param length the number of repetitions to do
 * @return ExperimentResult with the number of heads and the time taken
 */
ExperimentResult run_experiment(int length) {
    int start = clock();
    int total_heads = generate_unbiased_sequence(1e6);
    int end = clock();
    ExperimentResult result = {total_heads, (double)(end - start) / CLOCKS_PER_SEC};
    return result;
}

/**
 * Main function
*/
int main() {
    srand(time(NULL));
    ExperimentResult result = run_experiment(1e6);
    printf("Number of heads: %d\n", result.heads);
    printf("C Time: %f [s]\n", result.time);
}