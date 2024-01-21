def collect_numbers(original_permutation):
    n = len(original_permutation)
    inverse = [None] * n
    for i in range(n):
        inverse[original_permutation[i]] = i
    current = 0
    currentRound = 1
    for i in inverse:
        if i < current:
            currentRound += 1
            current = i
        else:
            current = i
    return currentRound
