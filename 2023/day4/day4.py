#! /usr/bin/env python3


def part1_and_part2():
    f = open("input.txt")
    lines = f.read().split("\n")[:-1]
    f.close()

    the_sum = 0
    matches_and_card_counts = []
    for line in lines:
        card, my_nums = line.split("|")
        card = set(card.split(":")[1].split())
        my_nums = set(my_nums.split())
        num_matches = len(card.intersection(my_nums))
        matches_and_card_counts.append([num_matches, 1])

        if num_matches > 0:
            the_sum += pow(2, num_matches - 1)

    for i in range(len(matches_and_card_counts)):
        matches, card_counts = matches_and_card_counts[i]
        for _ in range(card_counts):
            for j in range(matches):
                matches_and_card_counts[i+j+1][1] += 1

    print(the_sum)
    print(sum(map(lambda x: x[1], matches_and_card_counts)))


def main():
    part1_and_part2()


if __name__ == "__main__":
    main()
