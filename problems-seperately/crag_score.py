def crag_score(dice):
    dicesSum = sum(dice)

    def is_arithmetic_progression(lst):
        return all(lst[i] - lst[i - 1] == lst[1] - lst[0] for i in range(2, len(lst))) and not lst == [2,3,4] and not lst == [3,4,5]

    def checkCombinations():
        result = []
        for value in range(6, 0, -1):
            if value in dice:
                result.append(dice.count(value) * value)
        return max(result)

    if dicesSum == 13:
        if any(dice.count(i) == 2 for i in dice):
            return 50
        else:
            return 26
    elif any(dice.count(i) == 3 for i in dice):
        return 25
    elif is_arithmetic_progression(sorted(dice)):
        return 20
    else:
        return checkCombinations()
