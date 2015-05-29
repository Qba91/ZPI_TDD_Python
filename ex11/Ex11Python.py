# -*- coding: UTF-8 -*-

"""

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""

import math

sequenceLength = {}

def next_number(n):
    """
    Calculates the next element of the chain, according to the principle.
    
    Args:
        n:    the next number in the chain
    
    Returns:
        n/2         if n is even
        3 * n + 1   if n is odd
    """
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


def sequence(start):
    """
    returns the number of elements in the chain.
    """
    global sequenceLength
    seq = [1]
    n = start

    while n != 1 and n not in sequenceLength:
        seq.append(n)
        n = next_number(n)

    if n in sequenceLength:
        length = len(seq) + sequenceLength[n]
    else:
        length = len(seq)

    l = length
    for n in seq:
        sequenceLength[n] = l
        l -= 1

    return length


def longest_collatz_sequence():
    """
    Returns the number of the longest chain.
    """
    longest = 0
    start = 0
    for n in range(1, 1000000):
        l = sequence(n)
        if l > longest:
            longest = l
            start = n
    return start


print(longest_collatz_sequence())
