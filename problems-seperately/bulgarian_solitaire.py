def bulgarian_solitaire(piles, k):
    setK = set(range(1, k + 1))
    tempPiles = piles
    result = 0
    while True:
        if len(tempPiles) == k and set(tempPiles) == setK:
            return result

        result += 1

        newPile = len(tempPiles)
        tempPiles = [pile - 1 for pile in tempPiles]
        tempPiles = list(filter(lambda x: x != 0, tempPiles))
        tempPiles.append(newPile)
