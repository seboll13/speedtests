# Unbiased Coin Simulation

This project simulates an unbiased coin run using a biased coin across multiple programming languages. It showcases the implementation of the Von Neumann method for generating an unbiased sequence of coin flips from a biased coin. Supported languages include Python, C, JavaScript, and Mojo, with Rust coming soon.

## Project Structure

- `simulator.py`: Python implementation.
- `simulator.c`: C implementation.
- `simulator.js`: JavaScript implementation.
- `simulator.mojo`: Mojo implementation.
- `Makefile`: Contains commands for compiling and executing the simulations.

## Prerequisites

Ensure you have the following installed:
- Python
- GCC (for C)
- Node.js (for JavaScript)
- Mojo Runtime (for Mojo)

## Usage

To compile and run the simulations across all languages:
```
make all
make execute
```

To run a specific simulation:
- For Python: `make python`
- For Mojo: `make mojo`
- For Node.js: `make node`

To clean the directory (remove compiled files):
```
make clean
```

## Contributing

Contributions are welcome! If you'd like to add support for another language or improve existing implementations, please submit a pull request.

## License

This project is open source and available under the [MIT License](LICENSE.md).