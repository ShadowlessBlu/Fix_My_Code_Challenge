#!/usr/bin/python3
""" FizzBuzz"""
import sys


def fizzbuzz(num):
    """
    FizzBuzz function prints numbers from 1 to n separated by a space.
    - For multiples of three print "Fizz" instead of the number and for
      multiples of five print "Buzz".
    - For numbers which are multiples of both three and five print "FizzBuzz".
    """
    if num < 1:
        return

    res = []
    for i in range(1, num + 1):
        if (i % 3) == 0 and (i % 5) == 0:
            res.append("FizzBuzz")
        elif (i % 3) == 0:
            res.append("Fizz")
        elif (i % 5) == 0:
            res.append("Buzz")
        else:
            res.append(str(i))
    print(" ".join(res))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    number = int(sys.argv[1])
    fizzbuzz(number)
