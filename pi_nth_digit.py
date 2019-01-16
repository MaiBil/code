"""
Find PI to the Nth Digit - Enter a number and have the program
generate π (pi) up to that many decimal places. Keep a limit to
how far the program will go.
"""

from math import pi

def pi_nth_digit(n):
    """
    Return pi to the n-th decimal place
    :param n: number of decimal places to return
    :type n: int
    :return: pi with n decimal places
    :rtype: str
    """
    return '%.*f' % (n,pi) 


if __name__ == '__main__':
    correct_input = False
    while not correct_input:
        print("The total number of digits of pi must be between 1 and 51.")
        while True:
            try:
                precision = int(input("How many digits do you want pi to have? "))
            except:
                print("That was not a valid number!")
            else:
                break
        if precision > 1 and precision < 51:
            correct_input = True
    print(pi_nth_digit(precision))