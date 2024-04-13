use std::time::{Instant};
use rand::Rng;

const PROB: f64 = 0.4;
const SEQ_LEN: i32 = 1000000;

struct ExperimentResult {
    avg_heads: i32,
    exec_time: f64,
    min_time: f64,
    max_time: f64,
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
fn run_experiment(length: i32, rng: &mut impl Rng) -> ExperimentResult {
    let mut total_heads = 0;
    let mut times = Vec::new();
    for _ in 0..length {
        let start_time = Instant::now();
        total_heads += generate_unbiased_sequence(SEQ_LEN, rng);
        let end_time = Instant::now();
        let exec_time = (end_time - start_time).as_secs_f64();
        times.push(exec_time);
    }
    return ExperimentResult {
        avg_heads: total_heads / length,
        exec_time: times.iter().sum::<f64>() / length as f64,
        min_time: times.iter().fold(f64::INFINITY, |a, &b| a.min(b)),
        max_time: times.iter().fold(f64::NEG_INFINITY, |a, &b| a.max(b)),
    };
}

/// Main program.
fn main() {
    let length = 10;
    let mut rng = rand::thread_rng(); // Use a specific RNG instance
    println!("============ Running Rust Experiment ============");
    let res = run_experiment(length, &mut rng);
    println!("Average Heads : {}", res.avg_heads as i32);
    println!("Execution Time: {:.3} [s] (min: {:.3}, max: {:.3})", res.exec_time, res.min_time, res.max_time);
}
