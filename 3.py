def feed_animals(animals, portions):
    animals.sort()
    portions.sort()

    i = 0
    j = 0
    fed = 0

    while i < len(animals) and j < len(portions):
        if portions[j] >= animals[i]:
            fed += 1
            i += 1

        j += 1

    return fed