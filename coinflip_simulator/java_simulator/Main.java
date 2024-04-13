package coinflip_simulator.java_simulator;
import java.util.logging.Logger;
import java.util.stream.IntStream;
import java.util.DoubleSummaryStatistics;
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
    ExperimentResult runSimulation(int n) {
        int totalHeads = 0;
        double[] times = new double[n];
        for (int i = 0; i < n; i++) {
            long start = System.nanoTime();
            totalHeads += generateUnbiasedSequence(1000000);
            long end = System.nanoTime();
            times[i] = (end - start)/1e9;
        }
        double avgHeads = totalHeads / (double) n;
        DoubleSummaryStatistics stats = IntStream.range(0, n).mapToDouble(i -> times[i]).summaryStatistics();
        return new ExperimentResult(
            avgHeads, stats.getAverage(), stats.getMin(), stats.getMax()
        );
    }

    /**
     * Main program that runs the simulation and prints the results
     * @param args
     */
    public static void main(String[] args) {
        logger.setLevel(Level.INFO);
        Main main = new Main();
        ExperimentResult res = main.runSimulation(10);
        logger.log(Level.INFO, "============ Running Java Experiment ============");
        logger.log(Level.INFO, "Average Heads : {0}", res.getAvgHeads());
        logger.log(Level.INFO, "Execution Time: {0} [s] (min: {1}, max: {2})", new Object[]{res.getAvgTime(), res.getMinTime(), res.getMaxTime()});
        
    }
}