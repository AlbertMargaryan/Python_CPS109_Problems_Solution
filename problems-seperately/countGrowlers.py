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
