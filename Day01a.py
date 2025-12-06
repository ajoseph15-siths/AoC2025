# Create a list to hold the contents of the input file
myList = []

# Open the input file
# Strip any whitespaces from the line
# Append each line to the list myList
def open_file():
    with open("input.txt") as f:
        for x in f:
            myList.append(x.strip())

open_file()

#testLine = "R48"
# Set the beginning position of the dial
dial = 50
# A counter to count the number of "0"
zeroCounter = 0

# Takes in a line from the input file, converts the L/R# into a positive or negative number
def getDirectionAndNumber(inputLine):
    # The first character should be either L or R
    # Everything after the first character should be the number
    direction = inputLine[0]
    number = int(inputLine[1:])
    # If the number is greater than 99, you can chop off the 100s
    if number > 99:
        number = chopOffHundreds(number)
    # If the direction is L, you will make the number negative (same as subtracting)
    if direction == "L":
        number = number * -1
    return number

# Takes in a number that is greater than 99 and gets rid of all other places except tens and ones
def chopOffHundreds(numberToBeChopped):
    # convert the number to a string
    numAsString = str(numberToBeChopped)
    # and only keep the last two characters
    numAsString = numAsString[-2:]
    # return the number as an integer
    return int(numAsString)

# Takes in the dial's current position and the instructions (from getDirectionAndNumber)
# to move the dial to the next position
def turnTheDial(currentPosition, instruction):
    #print("Current Position: " + str(currentPosition))
    #print("Current Instruction: " + str(instruction))
    currentPosition += instruction
    #print("New position after turning dial is ", currentPosition)
    if currentPosition > 99 or currentPosition < -99:
        currentPosition = chopOffHundreds(currentPosition)
    if currentPosition < 0:
        currentPosition += 100
    # Check if the ending position is zero; if it is, then add one to the counter
    if currentPosition == 0:
        print("Current position is 0; adding 1 to the zero counter")
        global zeroCounter
        zeroCounter += 1
        print("Zero counter: " + str(zeroCounter))
    return currentPosition

# Part 1: Count how many times the dial stops at 0 at the end of an instruction
for line in myList:
    dial = turnTheDial(dial,getDirectionAndNumber(line))

# Part 2: Count how many times the dial passes 0, regardless if it stops or not

# Test line by line
#print(turnTheDial(50,getDirectionAndNumber("L68")))
#print(turnTheDial(82,getDirectionAndNumber("L30")))
#print(turnTheDial(52,getDirectionAndNumber("R48")))
#print(turnTheDial(0,getDirectionAndNumber("L5")))
#print(turnTheDial(95,getDirectionAndNumber("R60")))
#print(turnTheDial(55,getDirectionAndNumber("L55")))