'''def ryerson_letter_grade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'
'''


def is_ascending(items):
    isListAscending = True
    i = 1
    while i < len(items):
        if items[i] <= items[i - 1]:
            isListAscending = False
            break
        i += 1
    return isListAscending


def riffle(items, out=True):
    firstHalf = items[:int(len(items)) // 2]
    secondHalf = items[int(len(items)) // 2:]
    riffledList = []
    i = 0
    while i < len(firstHalf):
        if out:
            riffledList.append(firstHalf[i])
            riffledList.append(secondHalf[i])
        else:
            riffledList.append(secondHalf[i])
            riffledList.append(firstHalf[i])
        i += 1
    return riffledList


def only_odd_digits(num):
    numString = str(num)
    return all(int(digit) % 2 != 0 for digit in numString)


def is_cyclops(num):
    listNum = list(str(num))
    if len(listNum) % 2 == 0:
        return False
    else:
        if int(listNum[len(listNum) // 2]) == 0:
            for i, v in enumerate(listNum):
                if i != len(listNum) // 2 and int(v) == 0:
                    return False
            return True
        else:
            return False


def domino_cycle(items):
    isDomino = True
    for i, v in enumerate(items):
        if i == len(items) - 1:
            if v[1] != items[0][0]:
                isDomino = False
                break
        else:
            if v[1] != items[i + 1][0]:
                isDomino = False
                break
    return isDomino


def colour_trio(color):
    colorList = list(color)
    newColorList = []
    if len(colorList) == 1:
        return colorList[0]
    for i, v in enumerate(colorList):
        if i + 1 != len(colorList):
            v2 = colorList[i + 1]
            if v == v2:
                newColorList.append(v)
            elif (v == "r" or v2 == "r") and (v == "b" or v2 == "b"):
                newColorList.append("y")
            elif (v == "y" or v2 == "y") and (v == "b" or v2 == "b"):
                newColorList.append("r")
            elif (v == "r" or v2 == "r") and (v == "y" or v2 == "y"):
                newColorList.append("b")
    return colour_trio("".join(newColorList))


def count_dominators(items):
    if not items:
        return 0
    items.reverse()

    max_i = items[0]
    n = 1
    for x in items:
        if x > max_i:
            max_i = x
            n += 1
    return n


def extract_increasing(digits):
    if len(digits) == 1:
        return [int(digits[0])]

    previousDigit = int(digits[0])
    currentDigit = int(digits[1])
    result = [int(digits[0])]

    for i, v in enumerate(list(digits)):
        if not (i == 0 or i == len(digits) - 1):
            if currentDigit > previousDigit:
                result.append(currentDigit)
                previousDigit = currentDigit
                currentDigit = int(digits[i + 1])
            else:
                currentDigit = currentDigit * 10 + int(digits[i + 1])
        elif i == len(digits) - 1:
            if currentDigit > previousDigit:
                result.append(currentDigit)
    return result


def words_with_letters(words, letters):
    result = []

    for word in words:
        tempWord = word
        count = len(letters)

        for letter in letters:
            if tempWord.find(letter) < 0:
                break
            elif tempWord.find(letter) >= 0:
                tempWord = tempWord[int(tempWord.find(letter)) + 1:]
                count -= 1
        if count == 0:
            result.append(word)

    return result


def taxi_zum_zum(moves):
    directions = ["W", "N", "E", "S"]
    currentDirection = "N"
    currentLocation = (0, 0)

    for move in moves:
        if move == "F":
            x, y = currentLocation
            if currentDirection == "N":
                currentLocation = (x, y + 1)
            elif currentDirection == "S":
                currentLocation = (x, y - 1)
            elif currentDirection == "E":
                currentLocation = (x + 1, y)
            elif currentDirection == "W":
                currentLocation = (x - 1, y)
        elif move == "L":
            currentDirection = directions[directions.index(currentDirection) - 1]
        elif move == "R":
            currentDirection = directions[directions.index(currentDirection) - 3]
    return currentLocation


change = []
changeLen = []


def give_change(amount, coins):
    tempAmount = amount
    result = []
    for coin in coins:
        while tempAmount >= coin:
            tempAmount -= coin
            result.append(coin)
    return result


def coin_change_recursive(amount, denominations, memo={}):
    if amount == 0:
        return []

    if amount < 0:
        return None

    if amount in memo:
        return memo[amount]

    best_change = None
    for coin in denominations:
        remaining_amount = amount - coin
        remaining_change = coin_change_recursive(remaining_amount, denominations, memo)

        if remaining_change is not None:
            current_change = [coin] + remaining_change

            if best_change is None or len(current_change) < len(best_change):
                best_change = current_change

    memo[amount] = best_change
    return best_change


def safe_squares_rooks(n, rooks):
    safeRows = set()
    safeColumns = set()
    for x, y in rooks:
        safeRows.add(x)
        safeColumns.add(y)
    return n ** 2 - n * len(safeRows) - (n - len(safeRows)) * len(safeColumns)


def words_with_given_shape(words, shape):
    def cmp(a, b):
        return (a < b) - (a > b)

    def word_to_shape(word):
        return [cmp(ord(word[i]), ord(word[i + 1])) for i in range(len(word) - 1)]

    result = []
    for word in words:
        x = word_to_shape(word)
        if x == shape:
            result.append(word)

    return result


'''
def is_left_handed(pips):
    dice = [pips[0], pips[1], pips[2], 7 - pips[0], 7 - pips[1], 7 - pips[2]]
    permutations = []
    i = 4
    oneLocation = dice.index(1)
    while i != 0:
        if i == 4:
            permutations.append((dice[oneLocation], dice[oneLocation - 5], dice[oneLocation - 4]))
        elif i == 3:
            permutations.append((dice[oneLocation], dice[oneLocation - 4], dice[oneLocation - 2]))
        elif i == 2:
            permutations.append((dice[oneLocation], dice[oneLocation - 2], dice[oneLocation - 1]))
        elif i == 1:
            permutations.append((dice[oneLocation], dice[oneLocation - 1], dice[oneLocation - 5]))
        i -= 1
    for permutation in permutations:
        if permutation == (1, 2, 3):
            return True
        elif permutation == (1, 3, 2):
            return False
'''


def winning_card(trick, trump=None):
    if trump is None:
        return winning_card(trick, trick[0][1])
    else:
        vals = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace']

        trumpCards = []
        for x, y in trick:
            if trump in y:
                trumpCards.append((x, y))
        if trumpCards:
            maxCardNum = 0
            maxCard = ""
            for card in trumpCards:
                if int(vals.index(card[0]) + 1) > maxCardNum:
                    maxCardNum = int(vals.index(card[0]))
                    maxCard = card
            return maxCard
        else:
            return winning_card(trick, trick[0][1])


# import math
def knight_jump(knight, start, end):
    listKnight = list(knight)
    for i, v in enumerate(start):
        offset = abs(v - end[i])
        if offset in listKnight:
            listKnight.remove(offset)
        else:
            return False
    return True


def seven_zero(n):
    i = 1
    if n % 2 != 0 and n % 5 != 0:
        while True:
            d = "7" * i
            if int(d) % n == 0:
                return d
            i += 1

    while True:
        j = 0
        while j < i:
            d = "7" * (i - j) + "0" * j
            j += 1
            if int(d) % n == 0:
                return d
        i += 1


def can_balance(items):
    for i, v in enumerate(items):
        listBefore = items[:i][::-1]
        listAfter = items[i + 1:]

        beforeSum = sum((j + 1) * a for j, a in enumerate(listBefore))
        afterSum = sum((k + 1) * b for k, b in enumerate(listAfter))

        if beforeSum == afterSum:
            return i
    return -1


def josephus(n, k):
    result = []
    currentRound = list(range(1, n + 1))
    currentPerson = 0
    while len(currentRound) != 0:
        currentPerson = (currentPerson + k - 1) % len(currentRound)
        result.append(currentRound[currentPerson])
        del currentRound[currentPerson]
    return result


def group_and_skip(n, out, ins):
    coins = n
    result = []
    while coins != 0:
        result.append(coins % out)
        coins = ins * (coins // out)
    return result


def pyramid_blocks(n, m, h):
    x = h * (h - 1) // 2
    sumToH = (h - 1) * h * (2 * (h - 1) + 1) // 6
    balls = n * m * h + n * x + m * x + sumToH
    return balls


def count_growlers(animals):
    global growling
    growling = 0

    def growlingCount(items):
        global growling
        dogsCount = items.count("dog") + items.count("god")
        catsCount = items.count("cat") + items.count("tac")
        if dogsCount > catsCount:
            growling += 1

    for i, v in enumerate(animals):
        if v == "cat" or v == "dog":
            animalsToI = animals[0:i]
            growlingCount(animalsToI)
        else:
            animalsToI = animals[i + 1:]
            growlingCount(animalsToI)
    return growling


def bulgarian_solitaire(piles, k):
    setK = set(range(1, k + 1))
    tempPiles = piles
    result = 0
    while True:
        if len(tempPiles) == k and set(tempPiles) == setK:
            return result

        result += 1

        newPile = len(tempPiles)
        tempPiles = [pile - 1 for pile in tempPiles]
        tempPiles = list(filter(lambda x: x != 0, tempPiles))
        tempPiles.append(newPile)


def scylla_or_charybdis(moves, n):
    moves_length = len(moves)
    result = []
    k = 1
    while k <= moves_length and moves_length // n >= k:
        position = 0
        for i, step in enumerate(moves[k - 1::k]):
            if step == "-":
                position -= 1
            else:
                position += 1
            if abs(position) > n - 1:
                result.append([i, k])
                break
        k += 1
    return min(result, key=lambda x: x[0])[1]


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


def tukeys_ninthers(items):
    if len(items) == 1:
        return items[0]

    def find_median_three_elements(t):
        if t[0] <= t[1] <= t[2] or t[2] <= t[1] <= t[0]:
            return t[1]
        elif t[1] <= t[0] <= t[2] or t[2] <= t[0] <= t[1]:
            return t[0]
        else:
            return t[2]

    newItems = []
    for i in range(0, len(items), 3):
        tuple3 = items[i:i + 3]
        newItems.append(find_median_three_elements(tuple3))
    return tukeys_ninthers(newItems)


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


def crag_score(dice):
    dicesSum = sum(dice)

    def is_arithmetic_progression(lst):
        return all(lst[i] - lst[i - 1] == lst[1] - lst[0] for i in range(2, len(lst))) and not lst == [2,3,4] and not lst == [3,4,5]

    def checkCombinations():
        result = []
        for value in range(6, 0, -1):
            if value in dice:
                result.append(dice.count(value) * value)
        return max(result)

    if dicesSum == 13:
        if any(dice.count(i) == 2 for i in dice):
            return 50
        else:
            return 26
    elif any(dice.count(i) == 3 for i in dice):
        return 25
    elif is_arithmetic_progression(sorted(dice)):
        return 20
    else:
        return checkCombinations()

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


def count_carries(a, b):
    result = 0
    c = 0
    x, y = max(a,b), min(a,b)
    for i in range(1,len(str(x))+1):
        try:
            l = int(str(y)[-i])
        except:
            l = 0
        c = (int(str(x)[-i])+l+c)//10
        print(c, int(str(x)[-i])+l+c, int(str(x)[-i]),l,c)
        if not c == 0:
            result+=1

    return result

#def leibniz():

def expand_intervals(intervals):
    intervalsNew = intervals.split(",") if not intervals == [] else []
    result = []
    for i in intervalsNew:
        if "-" in i:
            j = i.index("-")
            x, y = int(i[:j]), int(i[j+1:])
            result.extend(list(range(x,y+1)))
        elif i:
            result.append(int(i))
    return result

def collapse_intervals(items):
    j = 0
    result = ''
    while j <= len(items)-1:
        start = items[j]
        end = 0
        while not j+1 == len(items) and items[j]+1==items[j+1]:
            j += 1
            end = items[j]
            if j+1 == len(items):
                end = items[j]
                break
        if end > 0:
            result += f'{start}-{end},'
        else:
            result += f'{start},'
        j+=1
    return result[:-1]

def candy_share(candies):
    result = 0
    while not all(k==0 or k==1 for k in candies):
        result+=1
        newCandies = candies.copy()
        for i, v in enumerate(candies):
            if v>=2:
                newCandies[i] = candies[i]-2
                newCandies[i-1] = candies[i-1]+1
                if i+1==len(candies):
                    newCandies[0] = candies[0]+1
                else:
                    newCandies[i+1] = candies[i+1]+1
                candies = newCandies.copy()
    return result

def nearest_smaller(items):
    result = []
    for i, v in enumerate(items):
        for k in range(1,max(len(items)-i+1, i)+1):
            start = 0 if i-k <= 0 else i-k
            end = len(items)-1 if i+k >= len(items) else i+k
            minInKRange = min(items[start:end+1])
            if not minInKRange == v:
                result.append(minInKRange)
                break
            if start == 0 and end == len(items)-1 or v==min(items):
                result.append(v)
                break
    return result


def duplicate_digit_bonus(n):
    def split_number_to_strings(number):
        number_str = str(number)
        result = [number_str[0]]

        for digit in number_str[1:]:
            if digit == result[-1][0]:
                result[-1] += digit
            else:
                result.append(digit)

        return result
    splitN = split_number_to_strings(n)
    lenSplit = len(splitN)
    sum = 0
    for j,i in enumerate(splitN):
        if len(i)>=2:
            if j+1==lenSplit:
                sum += 10**(len(i)-2)*2
            else:
                sum += 10 ** (len(i) - 2)
    return sum


def ordinal_transform(seed, j):
    result = seed.copy()
    def otrf(items):
        resultDict = {}
        for i,v in enumerate(items):
            try:
                resultDict[v].append([i, resultDict[v][-1][1] + 1])
            except:
                resultDict[v] = []
                resultDict[v].append([i, 1])
        result = [0]*len(items)
        for val, res in resultDict.items():
            for i in res:
                result[i[0]] = i[1]
        return result

    for k in range(0,j):
        try:
            return result[j]
        except:
            result.extend(otrf(result))


def squares_intersect(s1, s2):
    sq1 = (s1[0]+s1[2], s1[1]+s1[2])
    sq2 = (s2[0] + s2[2], s2[1] + s2[2])

    if (((sq1[1]>=s2[1] and s1[1]<sq2[1]) or (sq2[1]>=s1[1] and s2[1]<sq1[1])) and
        ((sq1[0]>=s2[0] and s1[0]<sq2[0]) or (sq2[0]>=s1[0] and s2[0]<sq1[0]))):
        return True
    else:
        return False


def brussels_choice_step(n, mink, maxk):
    def get_all_substrings(input_string):
        substrings = []
        n = len(input_string)

        for i in range(n):
            for j in range(i + 1, n + 1):

                if j-i>=mink and j-i<=maxk:
                    substring = input_string[i:j]
                    substrings.append([substring, i,j])

        return substrings
    result = []
    original = str(n)
    for i in get_all_substrings(str(n)):
        start = i[1]
        end = i[2]
        if int(i[0])%2==0:
            replacement = str(int(int(i[0])/2))
            new_string = original[:start] + replacement + original[end:]
            result.append(int(new_string))
        replacement = str(int(int(i[0]) * 2))
        new_string = original[:start] + replacement + original[end:]
        result.append(int(new_string))
    return sorted(result)


def count_corners(points):
    count = 0
    for i,v in enumerate(points):
        for second in points:
            if not second == v and second[0]==v[0] and second[1]-v[1]>0:
                h = second[1]-v[1]
                if (v[0]+h, v[1]) in points:
                    count += 1

    return count

def first_preceded_by_smaller(items, k=1):
    for i, v in enumerate(items):
        count = 0
        for j in items[:i+1]:
            if j<v:
                count += 1
        if count >= k:
            return v
    return None
