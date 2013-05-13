def capCheck(word):
# tests to see if the letter in the word is capitalized. Returns a list of
# the location of all capitalized letters in the word.
    location = -1
    capList = []
    for letter in word:
        location = location + 1
        # if the letter is NOT equal to it's lowercase equivalent.
        if not (letter == letter.lower()):
            capList.append(location)
    return capList
