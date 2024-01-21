def tukeys_ninthers(items):
    if len(items) == 1:
        return items[0]
    newItems = []
    for num in range(len(items) // 3):
        newItems.append((items[3*num+1] if items[3* num +1] > items[3* num + 2] else (items[3* num + 2] if items[3* num] > items[3* num + 2] else items[num * 3])) if items[num * 3] > items[3* num +1] else (items[3* num +1] if items[3* num +1] < items[3* num + 2] else (items[num * 3] if items[num * 3] > items[3* num + 2] else items[3* num + 2])))
    return tukeys_ninthers(newItems)
