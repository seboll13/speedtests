const PROB: f64 = 0.4;

/// Flips a biased coin once and returns the result.
/// 
/// Returns:
/// 0 if the coin lands on tails,
/// 1 otherwise.
fn flip_biased_coin() -> i32 {
    return if rand::random::<f64>() < PROB { 0 } else { 1 };
}

/// Uses the Von Neumann method to generate an unbiase run of coin flips.
/// The function loops over a pair of biased coins flips until both flips are different.
/// 
/// Returns:
/// 0 if the run is HT,
/// 1 if the run is TH.
fn get_unbiased_run() -> i32 {
    loop {
        let first = flip_biased_coin();
        let second = flip_biased_coin();
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
fn generate_unbiased_sequence(length: i32) -> i32 {
    let mut count = 0;
    for _ in 0..length {
        count += get_unbiased_run();
    }
    return count;
}

/// Main program.
fn main() {
    let start_time = std::time::Instant::now();
    let total_heads = generate_unbiased_sequence(1e6 as i32);
    let end_time = std::time::Instant::now();
    println!("Total heads: {}", total_heads);
    println!("Rust Time: {} [s]", (end_time - start_time).as_secs_f64());
}
