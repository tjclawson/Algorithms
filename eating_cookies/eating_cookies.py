#!/usr/bin/python

import sys


# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
    base_case = [1, 1, 2, 4]

    for i in range(4, n + 1):
        base_case.append(base_case[i - 1] + base_case[i - 2] + base_case[i - 3])

    return base_case[n]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies),
                                                                                    n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
