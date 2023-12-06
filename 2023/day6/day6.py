#! /usr/bin/env python3


# Brute force
def part1_and_part2(is_part_two):
    f = open("input.txt")
    lines = f.read().split("\n")[:-1]
    f.close()

    ts = lines[0].split()[1:]
    ds = lines[1].split()[1:]

    if is_part_two:
        ts = ["".join(ts)]
        ds = ["".join(ds)]

    prod = 1

    for t, d in zip(map(int, ts), map(int, ds)):
        num_ways = 0
        for i in range(1, t):
            time_left = t - i
            dist_traveled = time_left * i
            if dist_traveled > d:
                num_ways += 1
        prod *= num_ways

    print(prod)


# Math shortcut
def part1_and_part2_math(is_part_two):
    from math import sqrt
    f = open("input.txt")
    lines = f.read().split("\n")[:-1]
    f.close()

    ts = lines[0].split()[1:]
    ds = lines[1].split()[1:]

    if is_part_two:
        ts = ["".join(ts)]
        ds = ["".join(ds)]

    prod = 1

    for t, d in zip(map(int, ts), map(int, ds)):
        l_end = 1 + int((t - sqrt(t*t - 4*d)) / 2)
        r_end = int((t + sqrt(t*t - 4*d)) / 2)
        prod *= (r_end - l_end + 1)
    print(prod)


def main():
    part1_and_part2(False)
    part1_and_part2(True)
    part1_and_part2_math(False)
    part1_and_part2_math(True)


if __name__ == "__main__":
    main()
