
def reveal_cards(deck: list[int]):  # LeetCode Q.950.
    if len(deck) <= 1:
        return deck

    deck.sort()  # Sort from smallest to biggest.
    if len(deck) == 2:
        return deck

    desired_deck, idx = deck[-2:], -3  # Iteration starts from the 3rd biggest card.
    while len(desired_deck) != len(deck):
        desired_deck.insert(0, deck[idx])
        desired_deck.insert(1, desired_deck.pop(-1))
        idx -= 1

    return desired_deck
