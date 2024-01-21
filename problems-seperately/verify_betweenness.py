def verify_betweenness(original_permutation, tuples):
    n = len(original_permutation)
    inverse = [None] * n
    for i in range(n):
        inverse[original_permutation[i]] = i

    for tuple in tuples:
        if not (inverse[tuple[0]] < inverse[tuple[1]] < inverse[tuple[2]] or inverse[tuple[0]] > inverse[tuple[1]] >
                inverse[tuple[2]]):
            return False
    return True
