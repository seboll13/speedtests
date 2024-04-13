# Unbiased Coin Simulation

This project simulates an unbiased coin run using a biased coin across multiple programming languages. It showcases the implementation of the Von Neumann method for generating an unbiased sequence of coin flips from a biased coin. Supported languages include Python, Mojo, Java, JavaScript, C, and Rust. The idea is to optimise the simulation for speed and efficiency across all languages and compare the results.

## Project Structure

- `simulator.py`: Python implementation.
- `simulator.mojo`: Mojo implementation.
- `simulator.js`: JavaScript implementation.
- The C, Rust and Java implementations are all located in their respective directories, named `x_simulator`, where `x` is the language name.
- `Makefile`: Contains commands for compiling and executing the simulations.

## Prerequisites

Ensure you have the following installed:
- GCC (for C)
- Python 3.9+
- Java (for Java)
- Cargo (for Rust)
- Mojo Runtime (for Mojo)
- Node.js (for JavaScript)

## Usage

Type ```make all``` to compile and run the simulations across all languages. If you wish to only run a specific simulation, type ```make x```, where `x` is the language name. For example, to run the Python simulation, type ```make python```. Run ```make clean``` to remove compiled files.

## Contributing

Contributions are welcome! If you'd like to add support for another language or improve existing implementations, please submit a pull request.

## License

This project is open source and available under the [MIT License](LICENSE.md).