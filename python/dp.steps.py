#!/usr/bin/env python

# Copyright (c) 2015, jraman <https://github.com/jraman>

'''
Minimum steps to one.
The following three operations are allowed:
 * subtract 1
 * divide by 2, if divisible by 2
 * divide by 3, if divisible by 3
Problem: Given a positive integer, n, find the minimum number of steps to
         reduce it to 1 using the operations listed above.

Solution: Using dynamic programming.

F(n) = 0 if n == 0
       1 + min(F(n - 1), F(n/2), F(n/3)), else
'''

import collections


def get_min_steps(nn):
    # num_steps[i] holds the number of steps to go from (i + 1) to 1
    num_steps = [None] * (nn + 1)
    step_seq = collections.defaultdict(list)
    idx2step = [' - 1', ' / 2', ' / 3']

    num_steps[1] = 0
    for ii in xrange(2, nn + 1):
        minval = num_steps[ii - 1]
        if ii % 2 == 0:
            minval = min(minval, num_steps[ii / 2])
        if ii % 3 == 0:
            minval = min(minval, num_steps[ii / 3])
        num_steps[ii] = 1 + minval

    return num_steps[nn]


def test():
    for n in xrange(1, 11):
        print n, get_min_steps(n)


if __name__ == '__main__':
    import sys
    if sys.argv[1:]:
        for ii in sys.argv[1:]:
            print ii, get_min_steps(int(ii))
    else:
        test()
