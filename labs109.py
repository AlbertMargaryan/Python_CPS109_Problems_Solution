def first_preceded_by_smaller(items, k=1):
    for i, v in enumerate(items):
        count = 0
        for j in items[:i+1]:
            if j<v:
                count += 1
        if count >= k:
            return v
    return None