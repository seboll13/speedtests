from time import perf_counter_ns
from random import uniform

PROB: float = 0.4

def flip_biased_coin() -> int:
    """Flips a biased coin once and returns the result.
    
    Returns
    ----------
    int
        0 if the coin lands on tails, 1 if the coin lands on heads.
    """
    return 0 if uniform(0, 1) < PROB else 1

def get_unbiased_run() -> int:
    """Uses the Von Neumann method to generate an unbiase run of coin flips.
    The function loops over a pair of biased coins flips until both flips are different.
    
    Returns
    ----------
    int
        0 if the run is HT, 1 if the run is TH.
    """
    while True:
        flip1, flip2 = flip_biased_coin(), flip_biased_coin()
        if flip1 != flip2:
            return flip2

def generate_unbiased_sequence(length: int) -> int:
    """Generates an unbiased sequence of coin flips and counts the number of heads.
    
    Parameters
    ----------
    length : int
        The length of the unbiased sequence.
    
    Returns
    ----------
    int
        The number of heads in the unbiased sequence.
    """
    return sum(get_unbiased_run() for _ in range(length))

def main():
    """Main program.
    """
    start_time = perf_counter_ns()
    total_heads = generate_unbiased_sequence(1_000_000)
    end_time = perf_counter_ns()
    print(f'Total heads: {total_heads}')
    print(f"Python Time: {(end_time - start_time)/1e9} [s]")

if __name__ == '__main__':
    main()
