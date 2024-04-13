from time import time
from random import random_float64


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

fn run_experiment(n: Int) raises -> Tuple[Int, Float64]:
    """Runs the unbiased coin flip experiment n times.

    Args:
        n: The number of times to run the experiment.
    
    Returns:
        A tuple of the total number of heads and the time taken to run the experiment.
    """
    var start: Int = time._realtime_nanoseconds()
    var total_heads: Int = generate_unbiased_sequence(1_000_000)
    var end: Int = time._realtime_nanoseconds()
    return total_heads, Float64((end-start)/1e9)

fn main() raises -> NoneType:
    """Main program.
    """
    var res: Tuple[Int, Float64] = run_experiment(1)
    print("Total heads:", res.get[0, Int]())
    print("Mojo Time:", res.get[1, Float64](), "[s]")
    