# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-01

"""
The Tribonacci sequence is a series of numbers where each number is the sum of the three preceding ones. When starting with 0, 0 and 1, the first 10 numbers in the sequence are 0, 0, 1, 1, 2, 4, 7, 13, 24, 44.

Given an array containing the first three numbers of a Tribonacci sequence, and an integer representing the length of the sequence, return an array containing the sequence of the given length.

    Your function should handle sequences of any length greater than or equal to zero.
    If the length is zero, return an empty array.
    Note that the starting numbers are part of the sequence.
"""


def tribonacci_sequence(start_sequence, length):
    tribonacci = []

    if length > 2:
        tribonacci = start_sequence
        for i in range(2, length - 1):
            sum = tribonacci[i - 2] + tribonacci[i - 1] + tribonacci[i]
            tribonacci.append(sum)
    elif length == 2:
        tribonacci.append(start_sequence[0])
        tribonacci.append(start_sequence[1])
    elif length == 1:
        tribonacci.append(start_sequence[0])
    elif length == 0:
        tribonacci = []

    return tribonacci


ding = tribonacci_sequence([21, 32, 43], 1)
print(ding)
print(len(ding))
