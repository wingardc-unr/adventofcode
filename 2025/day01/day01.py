#! /usr/bin/env python3


def part1():
    f = open("input.txt")
    lines = f.read().split("\n")
    print(lines)
    f.close()

    position = 50
    num_stopped_at_zero = 0
    for line in lines[:-1]:
        direction = line[0]
        distance = int(line[1:])

        position = (position + (distance if direction == "R" else -distance)) % 100

        if position == 0:
            num_stopped_at_zero += 1

    print(num_stopped_at_zero)


def part2():
    f = open("test_input.txt")
    lines = f.read().split("\n")
    print(lines)
    f.close()

    old_position = 50
    position = 50
    num_stopped_at_zero = 0
    num_crossed_zero = 0
    for line in lines[:-1]:
        direction = line[0]
        distance = int(line[1:])

        if direction == "L":
            position = position - distance
            diff = old_position - position
        else:
            position = position + distance
            diff = position - old_position

        if position % 100 != 0 and old_position != 0:
            if distance >= 100:
                num_crossed_zero += distance // 100
            elif not 0 <= position <= 100:
                num_crossed_zero += 1

        position %= 100

        if position == 0:
            num_stopped_at_zero += 1

        print(old_position, ":", position, ":", diff, ":", num_stopped_at_zero, ":", num_crossed_zero)
        old_position = position

    print(num_stopped_at_zero + num_crossed_zero)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
