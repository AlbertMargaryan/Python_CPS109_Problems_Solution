def scylla_or_charybdis(moves, n):
    moves_length = len(moves)
    result = []
    k = 1
    while k <= moves_length and moves_length // n >= k:
        position = 0
        for i, step in enumerate(moves[k-1::k]):
            if step == "-":
                position -= 1
            else: position += 1
            if abs(position) > n-1:
                result.append([i, k])
                break
        k += 1
    return min(result, key=lambda x: x[0])[1]
