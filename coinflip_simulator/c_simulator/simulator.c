#include <time.h>
#include <stdlib.h>
#include <stdio.h>

#define PROB 0.4
#define SEQ_LEN 1000000
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define MAX(a, b) ((a) > (b) ? (a) : (b))

// Struct to store the result of an experiment
typedef struct {
    int avg_heads;
    float exec_time;
    float min_time;
    float max_time;
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
    int total_heads = 0;
    double times[length];
    double total_time = 0;
    double min_time = 1e9;
    double max_time = 0.0;
    for (int i = 0; i < length; i++) {
        clock_t start = clock();
        int heads = generate_unbiased_sequence(SEQ_LEN);
        clock_t end = clock();
        double exec_time = ((double) (end - start)) / CLOCKS_PER_SEC;
        total_heads += heads;
        total_time += exec_time;
        min_time = MIN(min_time, exec_time);
        max_time = MAX(max_time, exec_time);
        times[i] = exec_time;
    }
    return (ExperimentResult) {
        .avg_heads = total_heads / length,
        .exec_time = total_time / length,
        .min_time = min_time,
        .max_time = max_time
    };
}

/**
 * Main function
*/
int main() {
    srand(time(NULL));
    printf("============ Running C Experiment ============\n");
    ExperimentResult res = run_experiment(10);
    printf("Average Heads : %d\n", (int)res.avg_heads);
    printf("Execution Time: %.3f [s] (min: %.3f, max: %.3f)\n", res.exec_time, res.min_time, res.max_time);
    return 0;
}