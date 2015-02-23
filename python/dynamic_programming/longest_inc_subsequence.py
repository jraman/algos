'''
Longest Increasing Subsequence

Given a sequence, a_0 ... a_N, find the longest subsequence a_i0, a_i1, ... a_iK
such that a_ij < a_ik if ij < ik.
Example:
Given, 1 2 4 1 5 2 9 1 12 4 5 15 6 7
       ^ ^ ^   ^   ^    ^      ^
The longest subsequence is: 1 2 4 5 9 12 15

This can be solved using DP (dynamic programming).

Let L[j] be the longest sequence at index j.
 * Initialize L[j] = 1.
 * For each i < j, if a_i < a_j, then L[j] = max(L[j], L[i] + 1)
   This is O(n^2)
 * Then, iterate through L to find the maximum.  This is O(n)

Copyright (c) 2015, jraman <https://github.com/jraman>
'''


class LongestIncreasingSubsequenceFinder(object):
    def __init__(self, seq):
        self.seq = seq                          # a[i], i = 0 ... N-1
        self.seq_length = [1] * len(seq)        # L[i], i = 0 ... N-1
        self.prev_idx = [None] * len(seq)
        self.max_subseq_length = None
        self._process_subseq_lengths()

    def _process_subseq_lengths(self):
        'DP algorithm is executed here'
        for jj in xrange(1, len(self.seq)):
            for ii in xrange(jj):
                if self.seq[ii] < self.seq[jj]:
                    if self.seq_length[jj] <= self.seq_length[ii]:
                        self.seq_length[jj] = self.seq_length[ii] + 1
                        self.prev_idx[jj] = ii
        self.max_subseq_length = max(self.seq_length)

    def get_longest_length(self):
        return self.max_subseq_length

    def get_longest_subsequence(self):
        start_idx = self.seq_length.index(self.max_subseq_length)
        subseq = [self.seq[start_idx]]
        prev_idx = self.prev_idx[start_idx]
        while prev_idx is not None:
            subseq.append(self.seq[prev_idx])
            prev_idx = self.prev_idx[prev_idx]
        subseq.reverse()
        return subseq


def test1():
    data1 = [1, 2, 4, 1, 5, 2, 9, 1, 12, 4, 5, 15, 6, 7]
    data2 = range(10)
    data3 = [x for x in reversed(data2)]
    for data in [data1, data2, data3]:
        lis = LongestIncreasingSubsequenceFinder(data)
        print 'Data:', data
        print 'Longest Inc Subseq Length:', lis.get_longest_length()
        print 'Longest Inc Subseq:', lis.get_longest_subsequence()
        print


def test2():
    import random
    data = [random.randint(-100, 100) for _ in xrange(100)]
    lis = LongestIncreasingSubsequenceFinder(data)
    print 'Data:', data
    print 'Longest Inc Subseq Length:', lis.get_longest_length()
    print 'Longest Inc Subseq:', lis.get_longest_subsequence()


if __name__ == '__main__':
    test1()
    test2()
