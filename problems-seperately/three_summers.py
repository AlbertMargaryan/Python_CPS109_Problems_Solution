def three_summers(items, goal):
    newItems = items.copy()
    for k in items:
        newGoal = goal - k
        newItems.remove(k)
        i=0
        j = len(newItems)-1
        while i < j:
            x = newItems[i] + newItems[j]
            if x == newGoal:
                return True
            elif x < newGoal:
                i += 1
            else:
                j -= 1
    return False
