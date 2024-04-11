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

fn main() raises -> NoneType:
    """Main program.
    """
    var start: Int = time._realtime_nanoseconds()
    var total_heads: Int = generate_unbiased_sequence(1_000_000)
    var end: Int = time._realtime_nanoseconds()
    print('Total heads:', total_heads)
    print('Mojo Time:', (end-start)/1e9, '[s]')
    