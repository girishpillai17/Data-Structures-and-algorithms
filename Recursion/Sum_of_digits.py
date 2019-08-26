
"""Given an integer, create a function which returns the sum of all the individual 
digits in that integer. For example: if n = 4321, return 4+3+2+1"""


def sum_of_digit(n):
    if n == 0:
        return 0
    else:
        return n%10 + sum_of_digit(n//10)

print(sum_of_digit(4))

