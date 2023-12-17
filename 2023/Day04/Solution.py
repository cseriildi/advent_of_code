###################
## INPUT PARSING ##
###################

f = open('input.txt', 'r')
input = f.read().splitlines()

cards = dict()
for line in input:
    card_number = int(line.split(":")[0][5:])
    winners = line.split(":")[1].split("|")[0].split()
    my_numbers = line.split(":")[1].split("|")[1].split()
    cards[card_number] = {"winners": winners, "my_numbers": my_numbers }

#####################
## PART 1 SOLUTION ##
#####################

for card_number in cards:
    counter = 0
    for number in cards[card_number]["winners"]:
        if number in cards[card_number]["my_numbers"]:
            counter += 1

    cards[card_number]["matches"] = counter

all_points = sum([2 ** (cards[card_number]["matches"] - 1) for card_number in cards if cards[card_number]["matches"] != 0])

print("Part 1 Solution: ", all_points)

#####################
## PART 2 SOLUTION ##
#####################

for card_number in cards:
    cards[card_number]["count"] = 1

for card_number in cards:
    if cards[card_number]["matches"] != 0:
        for matches in range(1, cards[card_number]["matches"] + 1):
            cards[card_number + matches]["count"] += 1 * cards[card_number]["count"]

count_of_scratchcards = sum([cards[card_number]["count"] for card_number in cards])

print("Part 2 Solution: ", count_of_scratchcards)