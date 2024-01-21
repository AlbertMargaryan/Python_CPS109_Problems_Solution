def group_and_skip(n, out, ins):
    coins = n
    result = []
    while coins != 0:
        result.append(coins % out)
        coins = ins * (coins // out)
    return result
