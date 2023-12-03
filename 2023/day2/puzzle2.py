#! /usr/bin/env python3


import sys


MAX_R = 12
MAX_G = 13
MAX_B = 14



def puzzle1():
    f = open("input.txt")
    lines = f.read().split("\n")
    f.close()

    possible_sum = power_sum = 0

    for line in lines:
        if len(line) == 0:
            continue

        line_split = line.split(":")
        current_game = int(line_split[0].split(" ")[1])

        results = line_split[1].split(";")
        curr_r = curr_g = curr_b = 0
        for result in results:
            split_res = result.split(",")
            for c in split_res:
                curr_num = int(c.strip().split(" ")[0])
                if "red" in c and curr_num > curr_r:
                    curr_r = curr_num
                elif "green" in c and curr_num > curr_g:
                    curr_g = curr_num
                elif "blue" in c and curr_num > curr_b:
                    curr_b = curr_num

        power = curr_r * curr_g * curr_b
        power_sum += power

        if curr_r <= MAX_R and curr_g <= MAX_G and curr_b <= MAX_B:
            possible_sum += current_game

    print(possible_sum)
    print(power_sum)



def main():
    puzzle1()
#    puzzle2()


if __name__ == "__main__":
    main()
