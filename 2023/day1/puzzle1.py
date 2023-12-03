#! /usr/bin/env python3


import sys


def get_first_number(text):
    for c in text:
        if c.isdigit():
            return c

    # No digit found.  This is not expected.
    print("No digit found in: '", text, "'", sep="")
    raise Exception


def puzzle1():
    f = open("input.txt")
    lines = f.read().split("\n")
    f.close()

    the_sum = 0
    for line in lines:
        if len(line) > 0:
            num = int(get_first_number(line) + get_first_number(line[::-1]))
            the_sum += num

    print(the_sum)


def get_earliest_digit(text, digit_map):
    earliest = sys.maxsize
    the_earliest = ""

    for key in digit_map:
        index = text.find(key)
        if index < earliest and index >= 0:
            earliest = index
            the_earliest = digit_map[key]

    return the_earliest


def puzzle2():
    digits = {
        "one"   : "1",
        "two"   : "2",
        "three" : "3",
        "four"  : "4",
        "five"  : "5",
        "six"   : "6",
        "seven" : "7",
        "eight" : "8",
        "nine"  : "9",
        "1"     : "1",
        "2"     : "2",
        "3"     : "3",
        "4"     : "4",
        "5"     : "5",
        "6"     : "6",
        "7"     : "7",
        "8"     : "8",
        "9"     : "9"
    }
    digits_keys_backwards = {}
    for k,v in digits.items():
        digits_keys_backwards[k[::-1]] = v

    f = open("input.txt")
    lines = f.read().split("\n")
    f.close()

    the_sum = 0
    for line in lines:
        if len(line) > 0:
            num = int(get_earliest_digit(line, digits) + get_earliest_digit(line[::-1], digits_keys_backwards))
            the_sum += num

    print(the_sum)


def main():
    puzzle1()
    puzzle2()


if __name__ == "__main__":
    main()
