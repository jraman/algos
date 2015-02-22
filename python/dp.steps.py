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


class MinSteps(object):
    def __init__(self, nn):
        # num_steps[i] holds the number of steps to go from (i + 1) to 1
        self.nn = nn
        self.num_steps = [None] * (nn + 1)
        self.prev_step = [None] * (nn + 1)
        self._setup()

    def _setup(self):
        self.num_steps[1] = 0
        for ii in xrange(2, self.nn + 1):
            minval = self.num_steps[ii - 1]
            if ii % 2 == 0:
                minval = min(minval, self.num_steps[ii / 2])
            if ii % 3 == 0:
                minval = min(minval, self.num_steps[ii / 3])
            self.num_steps[ii] = 1 + minval

    def get_min_steps(self, ii):
        assert ii <= self.nn
        return self.num_steps[ii]


def test():
    stepper = MinSteps(10)
    for n in xrange(1, 11):
        print n, stepper.get_min_steps(n)


if __name__ == '__main__':
    import sys
    if sys.argv[1:]:
        for ii in sys.argv[1:]:
            ii = int(ii)
            stepper = MinSteps(ii)
            print ii, stepper.get_min_steps(ii)
    else:
        test()
