from functools import wraps
from time import perf_counter_ns
from random import uniform
from typing import Any, Callable, Tuple

PROB: float = 0.4
SEQ_LEN: int = 1_000_000

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

def run_experiment(n: int) -> dict:
    """Runs the unbiased sequence generation experiment n times.
    
    Parameters
    ----------
    n : int
        The number of times to run the experiment.
    
    Returns
    ----------
    dict
        A dictionary containing the average number of heads as well as some statistics
        about the execution time of the experiment.
    """
    total_heads = 0
    times = []
    for _ in range(n):
        heads, exec_time = generate_unbiased_sequence(SEQ_LEN)
        total_heads += heads
        times += [exec_time]
    total_time = sum(times)
    min_time, max_time = min(times), max(times)
    return {
        'avg_heads': total_heads/n,
        'exec_time': total_time/n,
        'min_time': min_time,
        'max_time': max_time
    }

def main():
    """Main program.
    """
    print('============ Running Python Experiment ============')
    runner = run_experiment(10)
    print(f'Average Heads : {int(runner["avg_heads"])}')
    print(f"Execution Time: {runner['exec_time']:.3f} [s] (min: {runner['min_time']:.3f}, max: {runner['max_time']:.3f})")

if __name__ == '__main__':
    main()
