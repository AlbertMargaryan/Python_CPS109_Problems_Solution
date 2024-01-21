def arithmetic_progression(items):
    if len(items) == 1:
        return (items[0], 0, 1)
    resultSet = []
    for k, num in enumerate(items):
        for i, num2 in enumerate(items[k + 1:]):
            currentSequence = [num, num2]
            stride = num2 - num
            for j in items[k + i + 2:]:
                if j - currentSequence[-1] == stride:
                    currentSequence.append(j)
            resultSet.append(tuple(currentSequence))
    result = max(resultSet, key=len)
    resultTuple = (result[0], result[1] - result[0], len(result))
    return resultTuple
