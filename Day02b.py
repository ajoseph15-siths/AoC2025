import re

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

# 1. Split the input file into items in a list
splitList = myList[0].split(",")

# 2. Create list to hold invalid IDs
invalidIDs = []

# 3. Make a list to hold the possible target sequences
targetSequences = []

def partTwo(splitList,targetSequences):
    # 4. For loop through each range
    for idRange in splitList:
        indexOfHyphen = idRange.find("-")
        # Find the minimum ID (before the -) and convert it to an integer
        minID = int(idRange[:indexOfHyphen])
        # Find the maximum ID (after the -) and convert it to an integer
        maxID = int(idRange[indexOfHyphen+1:])
        # 5. For loop through the IDs in the range, from the min to the max
        for id in range(minID,maxID+1):
            # 5a. clear the target sequences when beginning a new id
            targetSequences.clear()
            # 5b. generate new target sequences based on the new id
            targetSequences = generateTargetSequences(str(id),targetSequences)
            # 6. For loop through each target sequence (for each id in each range)
            # 7. REGEX the target sequence and ID
            if idIsAllRepeats(str(id),targetSequences):
                print(id,"is invalid; adding to invalid list")
                invalidIDs.append(id)

    print("Part 2 answer:",sumInvalidIDs(invalidIDs))

# 5b. Takes in ID and generates target sequences based on that ID
def generateTargetSequences(idAsString,targetSequences):
    firstHalf = idAsString[:len(idAsString) // 2]
    targetSequences.append(firstHalf)
    nextTargetSequence(firstHalf,targetSequences)
    return targetSequences

# 5b. Modifies the target sequence to find all possible target sequences
def nextTargetSequence(targetSequence,targetSequences):
    # Cut the last digit off the target sequence
    if len(targetSequence) > 1:
        targetSequence = targetSequence[:-1]
        targetSequences.append(targetSequence)
        nextTargetSequence(targetSequence,targetSequences)
    return targetSequences

# 7. Loop through all of the possible target sequences, checking each one against the ID
# If the string is empty after substituting the target sequence in the ID, it is INVALID
# If the string is NOT empty, then the ID is valid
def idIsAllRepeats(id, targetSequences):
    for sequence in targetSequences:
        x = re.sub(sequence,"",id)
        # print("sequence=",sequence,"id=",id,"x=",x)
        if not x:
            # print("Checking ID",id,"against",targetSequences,"...it's all repeats")
            return True
    return False

# 8. Sum invalid IDs
def sumInvalidIDs(invalidIDs):
    sum = 0
    for id in invalidIDs:
        sum += id
    return sum

partTwo(splitList,targetSequences)