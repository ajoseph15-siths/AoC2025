# Create a list to hold the contents of the input file
from operator import truediv

myList = []

# Open the input file
# Strip any whitespaces from the line
# Append each line to the list myList
def open_file():
    with open("input.txt") as f:
        for x in f:
            myList.append(x.strip())

open_file()

# Split the input file into items in a list
splitList = myList[0].split(",")

# Create list to hold invalid IDs
invalidIDs = []

# For loop through each splitList item
def partOne(splitList):
    # For loop through each range
    for range in splitList:
        indexOfHyphen = range.find("-")
        # Find the minimum ID (before the -) and convert it to an integer
        minID = int(range[:indexOfHyphen])
        # Find the maximum ID (after the -) and convert it to an integer
        maxID = int(range[indexOfHyphen+1:])
        # For loop through the IDs in the range, from the min to the max
        findInvalidInRange(invalidIDs, minID, maxID+1)
    print("Part 1 answer:",sumInvalidIDs(invalidIDs))

def findInvalidInRange(invalidIDs, minID, maxID):
    for id in range(minID, maxID):
        # Check the first half and the second half are equal; if yes, add one to the count
        if checkForRepeats(id):
            invalidIDs.append(id)

def checkForRepeats(id):
    # Convert the number to a string
    idAsString = str(id)
    # Check if the number has an even number of digits; if not, return false
    if len(idAsString) % 2 != 0:
        return False
    else:
        # Get the first half of the number
        firstHalf = idAsString[:len(idAsString)//2]
        # Get the second half of the number
        lastHalf = idAsString[len(idAsString)//2:]
        # Check if they're the same
        if firstHalf == lastHalf:
            return True
        else:
            return False

def sumInvalidIDs(invalidIDs):
    sum = 0
    for id in invalidIDs:
        sum += id
    return sum

partOne(splitList)