def award_points(house, points=10, reason="general excellence", ledger=None):
    if ledger is None:
        ledger = {}
    ledger[house] = ledger.get(house, 0) + points
    print(f"{house} +{points} ({reason}) -> total {ledger[house]}")
    return ledger
led = {}
led=award_points("Gryffindor")
led = award_points("Gryffindor", 50, "defeating a troll", led)
led = award_points("Slytherin", 30, ledger=led)
print(f"Final ledger: {led}")