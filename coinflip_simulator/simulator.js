let PROB = 0.4;

/**
 * Flips a biased coin once and returns the result.
 * 
 * @returns {number} 0 for tails, 1 for heads
 */
function flipBiasedCoin() {
  return Math.random() < PROB ? 0 : 1;
}

/**
 * Uses the Von Neumann method to generate an unbiased run of coin flips. 
 * The function loops over a pair of biased coin flips until both flips are different.
 * 
 * @returns {number} 0 if the run is HT, 1 if the run is TH
 */
function getUnbiasedRun() {
    while (true) {
        let first = flipBiasedCoin();
        let second = flipBiasedCoin();
        if (first !== second) {
            return second;
        }
    }
}

/**
 * Generates an unbiased sequence of coin flips and counts the number of heads.
 * 
 * @param {number} length of the unbiased sequence
 * @returns {number} the total number of heads in the sequence
 */
function generateUnbiasedSequence(length) {
    let heads = 0;
    for (let i = 0; i < length; i++) {
        heads += getUnbiasedRun();
    }
    return heads;
}

/**
 * Runs the experiment of generating an unbiased sequence of coin flips a given # of times.
 * 
 * @param {number} n number of experiments 
 * @returns {Array} [total_heads, time_elapsed]
 */
function runExperiment(n) {
    let start = performance.now();
    let total_heads = generateUnbiasedSequence(1e6);
    let end = performance.now();
    return [total_heads, (end-start)/1000];
}

let res = runExperiment(10);
console.log(`Total number of heads: ${res[0]}`);
console.log(`JS Time: ${res[1]} [s]`);