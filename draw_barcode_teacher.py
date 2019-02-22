"""
draw_barcode.py: Draw barcode representing a ZIP code using Turtle graphics
Authors: jsventek (Joe Sventek)

CIS 210 assignment 3, part 2, Fall 2015.
"""
import argparse	# Used in main program to obtain 5-digit ZIP code from command
                # line
import time	# Used in main program to pause program before exit
import turtle	# Used in your function to print the bar code

## Constants used by this program
SLEEP_TIME = 5	# number of seconds to sleep after drawing the barcode
ENCODINGS = [[1, 1, 0, 0, 0],	# encoding for '0'
             [0, 0, 0, 1, 1],	# encoding for '1'
             [0, 0, 1, 0, 1],   # encoding for '2'
             [0, 0, 1, 1, 0],	# encoding for '3'
             [0, 1, 0, 0, 1],	# encoding for '4'
             [0, 1, 0, 1, 0],	# encoding for '5'
             [0, 1, 1, 0, 0],	# encoding for '6'
             [1, 0, 0, 0, 1],	# encoding for '7'
             [1, 0, 0, 1, 0],	# encoding for '8'
             [1, 0, 1, 0, 0]	# encoding for '9'
            ]
SINGLE_LENGTH = 25

def compute_check_digit(digits):
    """
    Compute the check digit for use in ZIP barcodes
    args:
        digits: list of 5 integers that make up zip code
    returns:
        check digit as an integer
    """
    sum = 0
    for i in range(len(digits)):
        sum = sum + digits[i]
    check_digit = 10 - (sum % 10)
    if (check_digit == 10):
        check_digit = 0
    return check_digit

"""
Draw a single barcode using Turtle graphics

Inputs:
    my_turtle: the turtle to use to draw the barcode
    digit: integer, if 0 draw single height bar, otherwise double height bar
Outputs:
    draws single height bar if digit == 0, double height otherwise
    bar is drawn orthogonal to the current direction of the turtle
    cursor is moved 10 units along the current direction to be ready for
        the next bar
"""
def draw_bar(my_turtle, digit):
    my_turtle.left(90)
    if digit == 0:
        length = SINGLE_LENGTH
    else:
        length = 2 * SINGLE_LENGTH
    my_turtle.forward(length)
    my_turtle.up()
    my_turtle.backward(length)
    my_turtle.right(90)
    my_turtle.forward(10)
    my_turtle.down()

"""
Draws a US 5-digit zip code as a barcode

Inputs:
    my_turtle: the turtle to use to draw the barcode
    zip: an integer value, > 0 and < 100000
Outputs:
    draws the barcode corresponding to the zip code
"""
def draw_zip(my_turtle, zip):
## first back the turtle up so that the zip code is approximately centered
## in the window
    my_turtle.up()
    my_turtle.backward(150)
    my_turtle.down()

## convert the integer zip value to a list of 5 decimal digits
## note that this will generate an appropriate number of leading zeroes
    digits = []
    for i in range(5):
        digits.append(zip % 10)
        zip = zip // 10
    digits.reverse()	# reverse, so that digits[0] is highest order digit

## compute check digit, and append to the list of digits
    check_digit = compute_check_digit(digits)
    digits.append(check_digit)

## draw the starting frame bar
    draw_bar(my_turtle, 1)

## draw the 5-digit zip code and the check digit
    for i in range(len(digits)):
        encoding = ENCODINGS[digits[i]]
        for j in range(len(encoding)):
            draw_bar(my_turtle, encoding[j])

## draw the finishing frame bar
    draw_bar(my_turtle, 1)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("ZIP", type=int)
    args = parser.parse_args()
    zip = args.ZIP
    if zip <= 0 or zip > 99999:
        print("zip must be > 0 and < 100000, you provided", zip)
    else:
        my_turtle = turtle.Turtle()
        draw_zip(my_turtle, zip)
        time.sleep(SLEEP_TIME)

if __name__ == "__main__":
    main()
