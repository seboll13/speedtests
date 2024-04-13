from functools import wraps
from time import perf_counter_ns
from random import uniform
from typing import Any, Callable, Tuple

PROB: float = 0.4

def timer(func) -> Callable[..., Tuple[Any, float]]:
    """Decorator function to measure the execution time of a function.
    
    Parameters
    ----------
    func : function
        The function to be measured.
    
    Returns
    ----------
    Callable object
        The inner function that returns the execution time of the function.
    """
    @wraps(func)
    def inner(*args, **kwargs) -> Tuple[Any, float]:
        start_time = perf_counter_ns()
        result = func(*args, **kwargs)
        end_time = perf_counter_ns()
        return result, (end_time - start_time)/1e9
    return inner

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

@timer
def generate_unbiased_sequence(length: int) -> Tuple[int, float]:
    """Generates an unbiased sequence of coin flips and counts the number of heads.
    
    Parameters
    ----------
    length : int
        The length of the unbiased sequence.
    
    Returns
    ----------
    Tuple[int, float]
        The total number of heads and the execution time of the function (from the
        timer decorator)
    """
    return sum(get_unbiased_run() for _ in range(length))

def main():
    """Main program.
    """
    total_heads, exec_time = generate_unbiased_sequence(1_000_000)
    print(f'Total heads: {total_heads}')
    print(f"Python Time: {exec_time} [s]")

if __name__ == '__main__':
    main()
