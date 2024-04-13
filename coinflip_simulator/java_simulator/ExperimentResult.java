package coinflip_simulator.java_simulator;

public class ExperimentResult {
    private double avgHeads;
    private double avgTime;
    private double minTime;
    private double maxTime;

    public ExperimentResult(double avgHeads, double avgTime, double minTime, double maxTime) {
        this.avgHeads = avgHeads;
        this.avgTime = avgTime;
        this.minTime = minTime;
        this.maxTime = maxTime;
    }

    // Getters
    public double getAvgHeads() {
        return avgHeads;
    }

    public double getAvgTime() {
        return avgTime;
    }

    public double getMinTime() {
        return minTime;
    }

    public double getMaxTime() {
        return maxTime;
    }
}
