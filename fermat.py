import random

import math


def prime_test(N, k):
	# This is main function, that is connected to the Test button. You don't need to touch it.
	return fermat(N,k), miller_rabin(N,k)


def mod_exp(x, y, N):
    # You will need to implement this function and change the return value.
    if (y == 0):
        return 1
    z = mod_exp(x, math.floor(y/2), N)
    if (y % 2 == 0):
        return (z**2) % N
    else:
        return (x * (z**2)) % N


def fprobability(k):
    # You will need to implement this function and change the return value.
    return 1 - (1 / (2**k))


# TODO Whole function
def mprobability(k):
    # You will need to implement this function and change the return value.   
    return 0.0

# Fermat's little theorem tests the primality of a number.
def fermat(N,k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
	#
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.
    if (N == 1):
        return 'composite'
    for x in range(1, k):
        a = random.randint(1, N - 1) # Pick as many ints as we have k
        print(f'The value of a is {a}')
        print(f'The value of a^(N - 1) is {a^(N - 1)}\n')
        if (mod_exp(a, (N-1), N) != 1):
            return 'composite'
    return 'prime'


# TODO Whole function
def miller_rabin(N,k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
	#
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.
	return 'composite'
