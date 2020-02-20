#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    plays = ['rock', 'paper', 'scissors']
    my_list = [['rock'], ['paper'], ['scissors']]

    if n == 0:
        return [[]]
    if n == 1:
        return my_list

    power_to_raise_3_to = 2
    
    for i in range(n - 1):
        k = 0
        list_target_size = 3 ** power_to_raise_3_to

        while k < list_target_size:
            list_copy = my_list.copy()
            rocklist = my_list[k].copy()
            paperlist = my_list[k].copy()
            scissorlist = my_list[k].copy()

            rocklist.append(plays[0])
            list_copy.pop(k)
            list_copy.insert(k, rocklist)

            paperlist.append(plays[1])
            list_copy.insert(k + 1, paperlist)

            scissorlist.append(plays[2])
            list_copy.insert(k + 2, scissorlist)
            my_list = list_copy.copy()
            k += 3

        power_to_raise_3_to += 1

    return my_list


print(rock_paper_scissors(3))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
