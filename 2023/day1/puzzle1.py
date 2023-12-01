#! /usr/bin/env python3

# Fairly straightforward brute force approach.


def get_first_number(text):
    print("Checking '", text, "'", sep="")
    
    for c in text:
        if c.isdigit():
            return c

    # No digit found.  This is not expected.
    print("No digit found in: '", text, "'", sep="")
    raise Exception
        

def main():
    f = open("input.txt")
    lines = f.read().split("\n")

    the_sum = 0
    for line in lines:
        if len(line) > 0:
            num = int(get_first_number(line) + get_first_number(line[::-1]))
            the_sum += num

    print(the_sum)


if __name__ == "__main__":
    main()
