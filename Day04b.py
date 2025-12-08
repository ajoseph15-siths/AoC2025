# 0. Create a list to hold the contents of the input file
def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

grid = []
file_data = get_file_data("input.txt")
for line in file_data:
    row = []
    for x in line:
        row.append(x)
    grid.append(row)

# make a counter for the number of accessible rolls
# loop through each list, if there is a roll, check the 8 adjacent positions
# start in row 1, col 1, through row len(grid)-1, col len(grid[0])-1
# for each roll, you must have its own counter for #of rolls around it
# if it's accessible (< 4 rolls around), add 1 to the counter
def numberOfAccessibleRolls(grid,count):
    accessible_rolls = False
    for row in range(1, len(grid)-1):
        for col in range(1, len(grid[0])-1):
            if grid[row][col] == "@":
                if numberOfAdjacentRolls(grid, row, col) < 4:
                    count += 1
                    grid[row][col] = "."
                    accessible_rolls = True
    if accessible_rolls:
        numberOfAccessibleRolls(grid,count)
    else:
        print(count)
        return count

# make empty buffer
def addBorders(grid):
    rowLength = len(grid[0])
    # add a row of . at the top of the grid
    grid.insert(0,[])
    for x in range(rowLength):
        grid[0].append(".")
    # add a row of . at the bottom of the grid
    grid.append([])
    for x in range(rowLength):
        grid[-1].append(".")
    # add a . at the beginning and end of each row
    colHeight = len(grid)
    for y in grid:
        y.insert(0,".")
        y.append(".")
    return grid

# take in the grid and a position (row, column)
# check all 8 surrounding positions
# return the number of rolls around that position
def numberOfAdjacentRolls(grid,row,column):
    rolls = 0
    # check above
    if (grid[row-1][column]) == "@":
        rolls += 1
    # check below
    if (grid[row+1][column]) == "@":
        rolls += 1
    # check left
    if (grid[row][column-1]) == "@":
        rolls += 1
    # check right
    if (grid[row][column+1]) == "@":
        rolls += 1
    # check up left
    if (grid[row-1][column-1]) == "@":
        rolls += 1
    # check up right
    if (grid[row-1][column+1]) == "@":
        rolls += 1
    # check down left
    if (grid[row+1][column-1]) == "@":
        rolls += 1
    # check down right
    if (grid[row+1][column+1]) == "@":
        rolls += 1
    return rolls

grid = addBorders(grid)
numberOfAccessibleRolls(grid,0)