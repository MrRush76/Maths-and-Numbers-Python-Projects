integerSearch = int(input("Which Integer are you searching for?\n"))
rangeStart = int(input("Where do you want the search to start?\n"))
rangeEnd = int(input("Where do you want the search to end?\n"))
occurences = 0 # initializes a variable to count how many times the integer is found
for i in range(rangeStart,rangeEnd): #starts a loop starting where i is the start of the range and finishes at the end of the range
  occurence = str(i).find(str(integerSearch)) # use .find() to treat i as a string to "find" the integer returning a positive integer if the number is found and -1 if it is not 
  if occurence > -1: # checks if the number was found 
    occurences = occurences + 1 # increases the amount of occurences if the number is found 
print(occurences) # prints the number of times it was found