package coinflip_simulator.java_simulator;
import java.util.logging.Logger;
import java.util.stream.IntStream;
import java.util.logging.Level;

public class Main {
    private static final double PROB = 0.4;
    private static final Logger logger = Logger.getLogger(Main.class.getName());

    /**
     * Flips a biased coin once and returns the result
     * @return 0 for tails, 1 for heads
     */
    int flipBiasedCoin() {
        return Math.random() < PROB ? 0 : 1;
    }

    /**
     * Uses the Von Neumann method to generate an unbiased run of coin flips
     * The function loops over a pair of biased coin flips until both flips are different
     * @return 0 if the run is HT, 1 if the run is TH
     */
    int getUnbiasedRun() {
        while (true) {
            int first = flipBiasedCoin();
            int second = flipBiasedCoin();
            if (first != second)
                return second;
        }
    }

    /**
     * Generates an unbiased sequence of coin flips and counts the number of heads
     * @param length of the sequence
     * @return the total number of heads in the sequence
     */
    int generateUnbiasedSequence(int length) {
        return IntStream.range(
            0, length
        ).map(i -> getUnbiasedRun()).sum();
    }

    /**
     * Runs the experiment of generating an unbiased sequence of coin flips a given # of times
     * @param n number of times to run the experiment
     * @return a pair of the total number of heads and the time taken to run the experiment
     */
    Pair<Integer, Double> runSimulation(int n) {
        long start = System.nanoTime();
        int totalHeads = generateUnbiasedSequence(1000000);
        long end = System.nanoTime();
        return new Pair<>(totalHeads, (end - start)/1e9);
    }

    /**
     * Main program that runs the simulation and prints the results
     * @param args
     */
    public static void main(String[] args) {
        logger.setLevel(Level.INFO);
        Main main = new Main();
        Pair<Integer, Double> res = main.runSimulation(10);
        logger.log(Level.INFO, "Total heads: {0}", res.t);
        logger.log(Level.INFO, "Java Time: {0} [s]", res.u);
    }
}