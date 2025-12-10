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

get_ranges()

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

part_one(ids,ranges)