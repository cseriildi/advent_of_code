###################
## INPUT PARSING ##
###################

f = open('input.txt', 'r')
input = f.read().splitlines()

types = dict()
types["five_of_a_kind"] = {"form": [5] , "rank": 7}
types["four_of_a_kind"] = {"form": [1, 4] , "rank": 6}
types["full_house"] = {"form": [2, 3] , "rank": 5}
types["three_of_a_kind"] = {"form": [1, 1, 3] , "rank": 4}
types["two_pair"] = {"form": [1, 2, 2] , "rank": 3}
types["one_pair"] = {"form": [1, 1, 1, 2] , "rank": 2}
types["high_card"] = {"form": [1, 1, 1, 1, 1] , "rank": 1}

hands = list()
bids = list()

for line in input:
    hands.append(line.split()[0])
    bids.append(line.split()[1])

#######################
## Defining function ##
#######################

def camel_cards(hands_values, hands_jokers):
    ranking = list()
    for id, hand in enumerate(hands_jokers):

        distict_cards = list(set(hand))
        formula = list()
        for card in distict_cards:
            formula.append(hand.count(card))
        formula.sort()
        
        for typ in types:
            if formula == types[typ]["form"]:
                ranking.append([hands_values[id], types[typ]["rank"], bids[id]])

    # Ranking based on hand type and then value of hand
    ranked = sorted(ranking, key= lambda x: (x[1], x[0]))

    total_winnings = 0
    for rank in range(len(ranked)):

        # The winning for a hand is the product of the rank and the bid
        total_winnings += (rank+1) * int(ranked[rank][2]) 
    return total_winnings

#####################
## PART 1 SOLUTION ##
#####################

"""
In the game the order of the cards based on their value are A > K > Q > J > T > numbers 9 - 2 .
However these letters are not in ABC order, so to make the comparison easier we can replace them with e.g Z, Y, X, W, V
"""

part1_hands = hands.copy()
for i in range(len(part1_hands)):
    part1_hands[i] = part1_hands[i].replace("A", "Z").replace("K", "Y").replace("Q", "X").replace("J", "W").replace("T", "V")

print("Part 1 Solution: ", camel_cards(part1_hands, part1_hands))

#####################
## PART 2 SOLUTION ##
#####################

"""
Now the order of the cards has changed to A > K > Q > T > numbers 9 - 2 > J, so the value of J can be 1. 
But the J is now a Joker card, so to determine the hand type we can change it to the most common (other than J) card in the hand.
"""

part2_hands = hands.copy()
hands_with_jokers = hands.copy()

for i in range(len(part2_hands)):
    part2_hands[i] = part2_hands[i].replace("A", "Z").replace("K", "Y").replace("Q", "X").replace("J", "1").replace("T", "V")
    hands_with_jokers[i] = hands_with_jokers[i].replace("A", "Z").replace("K", "Y").replace("Q", "X").replace("T", "V")

    if hands_with_jokers[i]  != "JJJJJ":
        most_common = max(set(hands_with_jokers[i].replace("J", "")), key = hands_with_jokers[i].replace("J", "").count)
        hands_with_jokers[i] = hands_with_jokers[i].replace("J", most_common)

print("Part 2 Solution: ", camel_cards(part2_hands, hands_with_jokers))