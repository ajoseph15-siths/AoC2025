# 0. Create a list to hold the contents of the input file
ranges = []
ids = []

# Open the input file
# Strip any whitespaces from the line
# Append each line to the list myList
def get_ranges():
    with open("input.txt") as f:
        passedLineBreak = False
        for x in f:
            if not passedLineBreak and x != "\n":
                ranges.append(x.strip())
            elif x == "\n":
                passedLineBreak = True
            else:
                ids.append(x.strip())

# convert a range as a string into a list of lists
# containing the min and max values of the range
def converted_range(rangeAsString):
    listOfRanges = []
    for x in rangeAsString:
        indexOfHyphen = x.index("-")
        min = int(x[0:indexOfHyphen])
        max = int(x[indexOfHyphen + 1:])
        listOfRanges.append([min, max])
    listOfRanges.sort()
    return listOfRanges

# combine ranges
def combine_ranges(listOfRanges):
    combined = False
    # compare the first and second range.
    for i,r in enumerate(listOfRanges):
        minRange1 = listOfRanges[i][0]
        maxRange1 = listOfRanges[i][1]
        # get the minimum of the second range
        if i < len(listOfRanges)-1:
            minRange2 = listOfRanges[i+1][0]
            maxRange2 = listOfRanges[i+1][1]
            # if the second range minimum is within the first range (inclusive),
            if minRange1 <= minRange2 <= maxRange1:
                # then the two ranges can be combined into the first range
                newMin = min(minRange1, minRange2)
                newMax = max(maxRange1, maxRange2)
                listOfRanges[i] = [newMin, newMax]
                # delete the second range (it doesn't matter really)
                listOfRanges.pop(i+1)
                combined = True
    if combined:
        combine_ranges(listOfRanges)
    else:
        part_two(listOfRanges)
        return listOfRanges

# check if an id is within a given range
# return true or false
def inRange(id,range):
    indexOfHyphen = range.index("-")
    min = int(range[0:indexOfHyphen])
    max = int(range[indexOfHyphen+1:])
    if min <= int(id) <= max:
        return True
    else:
        return False

# loop through the ids
# check them against each range
def part_one(ids,ranges):
    count = 0
    for id in ids:
        idChecked = False
        for range in ranges:
            if inRange(id,range) and not idChecked:
                count += 1
                idChecked = True
                continue
    print(count)
    return count

# start a count
# loop through combined ranges
# for each range, calculate the number of fresh id's ((max-min)+1)
# add the number to the count
def part_two(combinedRanges):
    freshSum = 0
    for combinedRange in combinedRanges:
        min = combinedRange[0]
        max = combinedRange[1]
        difference = max - min
        freshSum += (difference + 1)
    print("Final # of fresh IDs =",freshSum)
    return freshSum

# get info from input file
get_ranges()
# make a sorted list of lists, where each list item is a list containing a min and max of a range
listOfRanges = converted_range(ranges)
# loop through all of the sorted list of ranges, combining when necessary
combine_ranges(listOfRanges)
# calculate number of fresh ids in the combined ranges
# print(part_two(x))