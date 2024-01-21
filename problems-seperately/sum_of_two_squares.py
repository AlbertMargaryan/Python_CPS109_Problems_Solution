import math
def sum_of_two_squares(n, i=0, j=None):
    l = int(math.sqrt(n))
    items = range(1,l+1)
    j = len(items)-1 if j is None else j
    while i < j:
        x = items[i]**2 + items[j]**2
        if x == n:
            return (j+1,i+1)
        elif x < n:
            i += 1
        else:
            j -= 1
    return False
