def readWord(): ##function that reads in the word from the user and returns it
    return input("Word: ")

word = readWord() ##gets the first word
longestWord = "" ##initialises the longestWord variable.
while word != ".": ##while the user hasn't entered a .
    if len(word) > len(longestWord): ##if the length of the word entered is longer than the longest word so far
        longestWord = word ##that word is the new longest
    word = readWord() ##read in the next word
print("Longest Word: " + longestWord) ##after . is entered, print the longest word.
