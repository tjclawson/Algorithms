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


# first_test = """
# def find_max_profit(prices):
#     max_profit = -float('inf')
#     for i in range(len(prices) - 1, -1, -1):
#         for j in range(0, i):
#             if prices[i] - prices[j] > max_profit:
#                 max_profit = prices[i] - prices[j]
#
#     return max_profit
#
# my_prices = [100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]
# find_max_profit(my_prices)
# """
#
# second_test = """
# def find_max_profit_skip(prices):
#     max_profit = -float('inf')
#     for i in range(len(prices) - 1, -1, -1):
#         if prices[i] >= max_profit:
#             for j in range(0, i):
#                 if prices[i] - prices[j] > max_profit:
#                     max_profit = prices[i] - prices[j]
#
#     return max_profit
#
# my_prices = [100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]
# find_max_profit_skip(my_prices)
# """
# print(timeit.timeit(first_test, number=100)/100)
# print(timeit.timeit(second_test, number=100)/100)

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
