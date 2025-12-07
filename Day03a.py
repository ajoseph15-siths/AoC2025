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

# 1. for each bank
def partOne(banks,highestJoltages):
    # 2. find the highest number in the bank
    for bank in banks:
        firstHighestNumber = highestNumberInBank(bank[0:-1])
        secondHighestNumber = highestNumberInBank(bank[firstHighestNumber[1]+1:])
        highestJoltage = firstHighestNumber[0]*10 + secondHighestNumber[0]
        highestJoltages.append(highestJoltage)

# 5. find the highest number in the bank
def highestNumberInBank(bank):
    highestNumber = 0
    indexOfHighestNumber = 0
    # 5. loop through the numbers in the bank, looking for the greatest one
    for indx,digit in enumerate(bank):
        # 6. if the highest number is NOT the last number in the bank:
        if int(digit) > highestNumber:
            # 6a. add the highest number as the 1st digit
            highestNumber = int(digit)
            indexOfHighestNumber = indx
    return highestNumber,indexOfHighestNumber

partOne(banks,highestJoltages)
print("Part 1 answer:",sum(highestJoltages))
