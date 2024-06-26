let PROB = 0.4;
let SEQ_LEN = 1000000;

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
 * @returns {Object} an object containing the average number of heads and some statistics about the execution time
 */
function runExperiment(n) {
    let totalHeads = 0;
    let times = [];
    for (let i = 0; i < n; i++) {
        let start = performance.now();
        let heads = generateUnbiasedSequence(SEQ_LEN);
        let end = performance.now();
        totalHeads += heads;
        times.push((end - start) / 1000);
    }
    let totalTime = times.reduce((a, b) => a + b, 0);
    let minTime = Math.min(...times);
    let maxTime = Math.max(...times);
    return {
        avgHeads: totalHeads/n,
        execTime: totalTime/n,
        minTime: minTime,
        maxTime: maxTime
    };
}

/**
 * Main function to run the experiment and print the results.
 */
function main() {
    console.log('============ Running JavaScript Experiment ============');
    let runner = runExperiment(10);
    console.log(`Average Heads : ${Math.floor(runner.avgHeads)}`);
    console.log(`Execution Time: ${runner.execTime.toFixed(3)} [s] (min: ${runner.minTime.toFixed(3)}, max: ${runner.maxTime.toFixed(3)})`);
}

main();