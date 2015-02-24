'''
Backtracking:
Find all the permutations of the characters in a string or elements in an array.

Note:
 * Time complexity: O(n!)
 * If letters are repeated in the input, the output set will have repeated strings.

Ref:
 * http://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
'''


def swap(array, ii, jj):
    tmp = array[jj]
    array[jj] = array[ii]
    array[ii] = tmp


def print_array(array):
    print ''.join(array)


def permute(array, idx=0):
    if idx == len(array) - 1:
        print_array(array)
        return

    for jj in xrange(idx, len(array)):
        swap(array, idx, jj)
        permute(array, idx + 1)
        swap(array, idx, jj)


def main(text):
    array = list(text)
    permute(array)


if __name__ == '__main__':
    import sys
    main(sys.argv[1])
