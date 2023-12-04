#! /usr/bin/env python3


from collections import defaultdict as dd
from math import prod


def is_symbol(c):
    return c != "." and not c.isdigit()


def has_neighbor_symbol(line_group, start_index, end_index, gear_map, num, line_index):
    prev_line, curr_line, next_line = line_group
    found_symbol = False

    # Check to the left.
    if start_index > 0 and is_symbol(curr_line[start_index - 1]):
        found_symbol = True
        if curr_line[start_index - 1] == "*":
            gear_map[f"{line_index}:{start_index-1}"].append(num)

    # Check to the right.
    if end_index < len(curr_line) - 1 and is_symbol(curr_line[end_index]):
        found_symbol = True
        if curr_line[end_index] == "*":
            gear_map[f"{line_index}:{end_index}"].append(num)

    # Check above.
    if prev_line is not None:
        for i in range(start_index, end_index):
            if is_symbol(prev_line[i]):
                found_symbol = True
                if prev_line[i] == "*":
                    gear_map[f"{line_index-1}:{i}"].append(num)

    # Check below.
    if next_line is not None:
        for i in range(start_index, end_index):
            if is_symbol(next_line[i]):
                found_symbol = True
                if next_line[i] == "*":
                    gear_map[f"{line_index+1}:{i}"].append(num)

    # Check left diagonals.
    if start_index > 0:
        if prev_line is not None and is_symbol(prev_line[start_index - 1]):
            found_symbol = True
            if prev_line[start_index - 1] == "*":
                gear_map[f"{line_index-1}:{start_index-1}"].append(num)
        if next_line is not None and is_symbol(next_line[start_index - 1]):
            found_symbol = True
            if next_line[start_index - 1] == "*":
                gear_map[f"{line_index+1}:{start_index-1}"].append(num)

    # Check right diagonals.
    if end_index < len(curr_line) - 1:
        if prev_line is not None and is_symbol(prev_line[end_index]):
            found_symbol = True
            if prev_line[end_index] == "*":
                gear_map[f"{line_index-1}:{end_index}"].append(num)
        if next_line is not None and is_symbol(next_line[end_index]):
            found_symbol = True
            if next_line[end_index] == "*":
                gear_map[f"{line_index+1}:{end_index}"].append(num)

    return found_symbol


def process_current_line(line_group, gear_map, line_index):
    line = line_group[1]
    i = the_sum = 0

    while i < len(line) - 1:
        if line[i].isdigit():
            # We found a number. Find its ending index.
            j = i + 1
            while j < len(line) and line[j].isdigit():
                j += 1
            the_num = int(line[i:j])

            # Check all the "neighbors" for symbols.
            if has_neighbor_symbol(line_group, i, j, gear_map, the_num, line_index):
                the_sum += the_num

            # We're done with this number, keep going.
            i = j
        else:
            i += 1

    return the_sum


def part1_and_part2():
    """
    For each number in a line, find the start and end index.
    Check all "adjacent" points for a symbol.
    If no symbol found, keep going to the next number.
    If found a symbol, add to the total and keep going.

    Part 2 was worked into part 1 for simplicity, at the cost
    of introducing bad design.
    """
    f = open("input.txt")
    lines = f.read().split("\n")[:-1]
    f.close()

    gear_map = dd(lambda : [])
    the_sum = line_index = 0
    prev_line = None
    for i in range(len(lines)):
        curr_line = lines[i]

        if i > 0:
            prev_line = lines[i-1]

        if i < len(lines) - 1:
            next_line = lines[i+1]
        else:
            next_line = None

        the_sum += process_current_line([prev_line, curr_line, next_line], gear_map, line_index)
        line_index += 1

    print(the_sum)
    print(sum([prod(nums) for nums in gear_map.values() if len(nums) == 2]))


def main():
    part1_and_part2()


if __name__ == "__main__":
    main()
