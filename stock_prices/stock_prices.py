#!/usr/bin/python

import argparse
import timeit


def find_max_profit(prices):
    max_profit = -float('inf')
    for i in range(len(prices) - 1, -1, -1):
        for j in range(0, i):
            if prices[i] - prices[j] > max_profit:
                max_profit = prices[i] - prices[j]

    return max_profit


def find_max_profit_skip(prices):
    max_profit = -float('inf')
    for i in range(len(prices) - 1, -1, -1):
        if prices[i] >= max_profit:
            for j in range(0, i):
                if prices[i] - prices[j] > max_profit:
                    max_profit = prices[i] - prices[j]

    return max_profit


def find_max_profit_linear(prices):
    current_min = float('inf')
    current_max_profit = -float('inf')
    for p in prices:
        if p - current_min > current_max_profit:
            current_max_profit = p - current_min
        if p < current_min:
            current_min = p
    return current_max_profit


first_test = """
import random


def find_max_profit(prices):
    max_profit = -float('inf')
    for i in range(len(prices) - 1, -1, -1):
        for j in range(0, i):
            if prices[i] - prices[j] > max_profit:
                max_profit = prices[i] - prices[j]

    return max_profit

find_max_profit(random.sample(range(0, 10000), 1000))
"""

second_test = """

import random


def find_max_profit_skip(prices):
    max_profit = -float('inf')
    for i in range(len(prices) - 1, -1, -1):
        if prices[i] >= max_profit:
            for j in range(0, i):
                if prices[i] - prices[j] > max_profit:
                    max_profit = prices[i] - prices[j]

    return max_profit

find_max_profit_skip(random.sample(range(0, 10000), 1000))
"""

third_test = """
import random

def find_max_profit_linear(prices):
    current_min = float('inf')
    current_max_profit = -float('inf')
    for p in prices:
        if p - current_min > current_max_profit:
            current_max_profit = p - current_min
        if p < current_min:
            current_min = p
    return current_max_profit
    

find_max_profit_linear(random.sample(range(0, 10000), 1000))
"""

first_sum = 0
second_sum = 0
third_sum = 0

for i in range(100):
    first_sum += timeit.timeit(first_test, number=100) / 100
    second_sum += timeit.timeit(second_test, number=100) / 100
    third_sum += timeit.timeit(third_test, number=100) / 100


print(f"First: {first_sum / 100}")
print(f"Second: {second_sum / 100}")
print(f"Third: {third_sum / 100}")

# results from above test, took about 15 minutes to run
# First: 0.006794132146539994
# Second: 0.0002013778457999989
# Third: 0.00010037239724000194

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
