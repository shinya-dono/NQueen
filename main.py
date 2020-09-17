import argparse
import time
import matplotlib.pyplot as plt

from Permutations import NQueensP
from Recursion import NQueensR

parser = argparse.ArgumentParser()

parser.add_argument("numbers", nargs="+", type=int)
parser.add_argument("-t", "--chart-time", action="store_true", dest="chart_time")
parser.add_argument("-d", "--draw", action="count", default=0, dest="draw_level")
parser.add_argument("-b", "--brute-force", action="store_true", dest="bf_mode")

args = parser.parse_args()

if len(args.numbers) < 2:
    numbers = range(1, args.numbers[0] + 1)
else:
    numbers = args.numbers

if args.chart_time:
    times = []
    labels = []
    if args.bf_mode:
        for i in numbers:
            start_time = time.process_time()
            NQueensP(i, args.draw_level)
            times.append(time.process_time() - start_time)
            labels.append(i)
    else:
        for i in numbers:
            start_time = time.process_time()
            NQueensR(i, args.draw_level)
            times.append(time.process_time() - start_time)
            labels.append(i)

    plt.title(" calculation time for given N's ")
    plt.xlabel(" N ")
    plt.ylabel(" execution time in second(s) ")
    plt.bar(labels, times, align="center")
    plt.show()
    # plt.savefig("times.png")


elif args.bf_mode:
    for i in numbers:
        input(f"you are about to see possibilities for N={i}, press enter to continue.")
        start_time = time.process_time()
        NQueensP(i, args.draw_level)
        print(f"took {time.process_time() - start_time} to calculate possibilities for N={i}")

else:
    for i in numbers:
        input(f"you are about to see possibilities for N={i}, press enter to continue.")
        start_time = time.process_time()
        NQueensR(i, args.draw_level)
        print(f"took {time.process_time() - start_time} to calculate possibilities for N={i}")
