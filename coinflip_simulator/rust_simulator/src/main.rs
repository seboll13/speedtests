use std::time::{Instant};
use rand::Rng;

const PROB: f64 = 0.4;

struct ExperimentResult {
    total_heads: i32,
    exec_time: f64,
}

/// Flips a biased coin once and returns the result.
/// 
/// Returns:
/// 0 if the coin lands on tails,
/// 1 otherwise.
#[inline]
fn flip_biased_coin(rng: &mut impl Rng) -> i32 {
    return if rng.gen::<f64>() < PROB { 0 } else { 1 };
}

/// Uses the Von Neumann method to generate an unbiase run of coin flips.
/// The function loops over a pair of biased coins flips until both flips are different.
/// 
/// Returns:
/// 0 if the run is HT,
/// 1 if the run is TH.
fn get_unbiased_run(rng: &mut impl Rng) -> i32 {
    loop {
        let first = flip_biased_coin(rng);
        let second = flip_biased_coin(rng);
        if first != second {
            return second;
        }
    }
}

/// Generates an unbiased sequence of coin flips and counts the number of heads.
/// 
/// Args:
/// length: The length of the sequence.
/// 
/// Returns:
/// The number of heads in the sequence.
fn generate_unbiased_sequence(length: i32, rng: &mut impl Rng) -> i32 {
    return (0..length).map(|_| get_unbiased_run(rng)).sum();
}

/// Runs the coin flip experiment a given number of times.
///
/// Args:
/// length: The length of the sequence.
/// rng: The random number generator.
///
/// Returns:
/// The number of heads in the sequence and the execution time.
fn run_experiment(_length: i32, rng: &mut impl Rng) -> ExperimentResult {
    let start_time = Instant::now();
    let total_heads = generate_unbiased_sequence(1000000, rng);
    let end_time = Instant::now();
    return ExperimentResult {
        total_heads,
        exec_time: (end_time - start_time).as_secs_f64(),
    };
}

/// Main program.
fn main() {
    let length = 10;
    let mut rng = rand::thread_rng(); // Use a specific RNG instance
    let res = run_experiment(length, &mut rng);
    println!("Total heads: {}", res.total_heads);
    println!("Rust Time: {} [s]", res.exec_time);
}
