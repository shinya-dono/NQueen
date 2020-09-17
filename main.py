import argparse
import time
import matplotlib.pyplot as plt
from algorithms.Permutations import NQueensP
from algorithms.Recursion import NQueensR

# creating parser to parse user inputs
parser = argparse.ArgumentParser()

# takes array of N's or N from user
parser.add_argument("numbers", nargs="+", type=int)

# checks if the user wants to have a chart of execution times
parser.add_argument("-t", "--chart-time", action="store_true", dest="chart_time")

# verbosity of algorithms
parser.add_argument("-d", "--draw", action="count", default=0, dest="draw_level")

# uses Permutations algorithm instead of recursive algorithm
parser.add_argument("-b", "--brute-force", action="store_true", dest="bf_mode")

# done parsing
args = parser.parse_args()

# check if user has entered an array of N's or just a single N
if len(args.numbers) < 2:
    #
    numbers = args.numbers[0]
else:
    numbers = args.numbers

# execute algorithms but stores executions time
if args.chart_time:
    # empty arrays for X and Y of our plot
    times = []
    queens = []
    """
    user definitely doesnt wants to have a plot with one data, 
    so assuming that user wants to plot time for queens between 1 and N
    """
    if len(numbers) < 2:
        numbers = range(1, args.numbers[0] + 1)

    # execute algorithms
    if args.bf_mode:
        for i in numbers:

            # using process time for raw and accurate output
            start_time = time.process_time()

            # calling algorithm
            NQueensP(i, args.draw_level)

            # calculating delta time
            times.append(time.process_time() - start_time)

            # adding X label
            queens.append(i)
    else:
        for i in numbers:
            # using process time for raw and accurate output
            start_time = time.process_time()
            # calling algorithm
            NQueensR(i, args.draw_level)

            # calculating delta time
            times.append(time.process_time() - start_time)

            # adding X label
            queens.append(i)

    # configuring plot
    plt.title(" calculation of execution time for given N's ")
    plt.xlabel(" N ")
    plt.ylabel(" execution time in second(s) ")
    plt.bar(queens, times, align="center")

    # can either view the plot or
    plt.show()
    # uncomment next line to save the plot as times.png
    # plt.savefig("times.png")

# executing algorithms without charting the times
elif args.bf_mode:
    for i in numbers:
        """
        preventing algorithm from showing the out put until user confirms
        in order to avoid showing large unreadable output 
        """
        input(f"you are about to see possibilities for N={i}, press enter to continue.")
        # using process time for raw and accurate output
        start_time = time.process_time()
        # calling algorithm
        NQueensP(i, args.draw_level)

        # calculating delta time
        print(f"took {time.process_time() - start_time} to calculate possibilities for N={i}")

else:
    for i in numbers:
        input(f"you are about to see possibilities for N={i}, press enter to continue.")
        # using process time for raw and accurate output
        start_time = time.process_time()
        # calling algorithm
        NQueensR(i, args.draw_level)

        # calculating delta time
        print(f"took {time.process_time() - start_time} to calculate possibilities for N={i}")
