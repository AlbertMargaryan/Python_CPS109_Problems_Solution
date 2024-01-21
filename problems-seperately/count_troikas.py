def count_troikas(items):
    position_dict = {}
    result = 0
    for index, element in enumerate(items):
        if element in position_dict:
            position_dict[element].append(index)
        else:
            position_dict[element] = [index]

    for item in set(items):
        d = position_dict.get(item)
        if len(d) < 3:
            continue
        for pos, i1 in enumerate(d):
            for i2 in d[pos + 1:]:
                if i2 + (i2 - i1) in d:
                    result += 1
    return result
