# 0. Create a list to hold the contents of the input file
banks = []

# Open the input file
# Strip any whitespaces from the line
# Append each line to the list myList
def open_file():
    with open("input.txt") as f:
        for x in f:
            banks.append(x.strip())

open_file()

# 1. make a list to hold the highest joltages
highestJoltages = []

def highestNumberInBank(bank,startIndex,endIndex,joltage,highestJoltages):
    highestNumber = 0
    indexOfHighestNumber = -1
    # loop through the numbers in the bank, looking for the greatest one
    for index,digit in enumerate(bank):
        # if the current digit is greater than the current highest number,
        # and within the start and end indices,
        # replace the highest number with the current digit
        if int(digit) > highestNumber and index >= startIndex and index < endIndex:
            # add the highest number as the 1st digit
            highestNumber = int(digit)
            indexOfHighestNumber = index
    joltage = joltage + str(highestNumber)
    if len(joltage) == 12:
        highestJoltages.append(int(joltage))
        return joltage
    else:
        # call again
        startIndex = indexOfHighestNumber+1
        endIndex = endIndex+1
        highestNumberInBank(bank,startIndex,endIndex,joltage,highestJoltages)

def partTwo(banks,highestJoltages,numberOfBatteries):
    # 2. find the highest number in the bank
    for bank in banks:
        # calculate the end index
        endIndex = len(bank) - numberOfBatteries + 1
        highestNumberInBank(bank,0,endIndex,"",highestJoltages)
    print(highestJoltages)

partTwo(banks,highestJoltages, 12)
print("Part 2 answer:",sum(highestJoltages))