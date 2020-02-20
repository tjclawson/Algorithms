#!/usr/bin/python

import sys


# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
    base_case = [1, 1, 2]

    for i in range(3, n):
        base_case.append(base_case[0] + base_case[1] + base_case[2])
        base_case.pop(0)

    return base_case[n] if n < 3 else sum(base_case)

print(eating_cookies(1000000))
if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies),
                                                                                    n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
