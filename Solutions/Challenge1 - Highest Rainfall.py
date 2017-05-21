def readInput(): ##function to read in input from the user
    return input("Please enter the rainfall: ")

rainfall = readInput(); ##read in the rainfall

rainfallSplit = rainfall.split(','); ##split the string into an array by the commas
maximum = 0.0 ##initialise a variable to store the rainfall
for word in rainfallSplit: ##for each rainfall in the array
    if float(word) > maximum: ##if the rainfall is greater than the current highest, converting the string to a double to compare it
        maximum = float(word) ##new max is this rainfall
        
print("Highest Rainfall: " + str(maximum)) ##print out the highest rainfall
