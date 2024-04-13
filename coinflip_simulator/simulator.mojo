from time import time
from random import random_float64, seed
from collections import Dict, List


fn flip_biased_coin() raises -> Int:
    """Flips a biased coin once and returns the result.

    Returns:
        1 if the coin flip is heads, 0 if the coin flip is tails.
    """
    return 0 if random_float64() < 0.4 else 1

fn get_unbiased_run() raises -> Int:
    """Uses the Von Neumann method to generate an unbiased run of coin flips.
    The function loops over a pair of biased coin flips until both flips are different.

    Returns:
        0 if the run is HT, 1 if the run is TH.
    """
    while True:
        var first: Int = flip_biased_coin()
        var second: Int = flip_biased_coin()
        # w.p. 2*p*(1-p), we stop and return the result
        if first != second:
            return second

fn generate_unbiased_sequence(length: Int) raises -> Int:
    """Generates an unbiased sequence of coin flips and counts the number of heads.

    Args:
        length: The number of coin flips to generate.
    
    Returns:
        The number of heads in the sequence.
    """
    var heads: Int = 0
    for _ in range(length):
        heads += get_unbiased_run()
    return heads

fn run_experiment(n: Int) raises -> Dict[String, Float64]:
    """Runs the unbiased coin flip experiment n times.

    Args:
        n: The number of times to run the experiment.
    
    Returns:
        A tuple of the total number of heads and the time taken to run the experiment.
    """
    var total_heads: Int = 0
    var total_time: Float64 = 0.0
    var min_time: Float64 = 0.0
    var max_time: Float64 = 0.0
    var times: List[Float64] = List[Float64]()
    for idx in range(n):
        var start: Float64 = time._realtime_nanoseconds()
        total_heads += generate_unbiased_sequence(1_000_000)
        var end: Float64 = time._realtime_nanoseconds()
        var elapsed: Float64 = (end - start) / 1e9
        if idx == 0:
            min_time = elapsed
            max_time = elapsed
        times.append(elapsed)
        total_time += elapsed
        if elapsed < min_time:
            min_time = elapsed
        if elapsed > max_time:
            max_time = elapsed
    var stats: Dict[String, Float64] = Dict[String, Float64]()
    stats["avg_heads"] = total_heads / n
    stats["exec_time"] = total_time / n
    stats["min_time"] = min_time
    stats["max_time"] = max_time
    return stats

fn main() raises -> NoneType:
    """Main program.
    """
    print("============ Running Mojo Experiment ============")
    var res: Dict[String, Float64] = run_experiment(10)
    print('Average Heads : ', res['avg_heads'].to_int())
    print('Execution Time: ', res['exec_time'], '[s] (min: ', res['min_time'], ', max: ', res['max_time'], ')')
    