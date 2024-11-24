class MasterSlaveDFlipFlop:
    def __init__(self):
        self.master = 0  # Stores the state of the master flip-flop
        self.slave = 0   # Stores the state of the slave flip-flop

    def clock_cycle(self, d, clock):
        """
        Simulate one clock cycle.
        :param d: Input (Data)
        :param clock: Clock signal (1 for HIGH, 0 for LOW)
        """
        if clock == 1:  # When clock is HIGH, master follows D
            self.master = d
        elif clock == 0:  # When clock is LOW, slave follows master
            self.slave = self.master

    def output(self):
        """
        Get the current state of the flip-flop.
        :return: Slave output (Q)
        """
        return self.slave


# Testing the Master-Slave D Flip-Flop
flip_flop = MasterSlaveDFlipFlop()

# Simulating input and clock cycles
print("D\tClock\tQ")
inputs = [(1, 1), (1, 0), (0, 1), (0, 0), (1, 1), (1, 0)]  # (D, Clock) pairs

for d, clock in inputs:
    flip_flop.clock_cycle(d, clock)
    print(f"{d}\t{clock}\t{flip_flop.output()}")
