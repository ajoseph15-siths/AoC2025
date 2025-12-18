# 0. Create a list to hold the contents of the input file
def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

# print the grid
def print_grid(grid):
    for row in grid:
        for x in row:
            print(x,end="")
        print("\n")

# add extra row to bottom
# make empty buffer
def add_borders(grid):
    rowLength = len(grid[0])
    # add a row of . at the bottom of the grid
    grid.append([])
    for x in range(rowLength):
        grid[-1].append("0")
    return grid

# replace S with |
def replace_s_with_one(grid):
    for r,row in enumerate(grid):
        for c,col in enumerate(row):
            if grid[r][c] == "S":
                grid[r][c] = 1
            if grid[r][c] == ".":
                grid[r][c] = 0
    return grid

def part_two(grid):
    for r,row in enumerate(grid):
        if 0 < r < len(grid)-2:
            sum = 0
            for c,col in enumerate(row):
                if grid[r][c] != "^" and grid[r-1][c] != "^":
                    # look up
                    grid[r][c] = grid[r-1][c]
                    sum += grid[r-1][c]
                    # look up/right and up/left
                    if c < len(row)-1:
                        # check up and to the right
                        if grid[r][c + 1] == "^":
                            grid[r][c] += int(grid[r - 1][c + 1])
                            sum += int(grid[r-1][c + 1])
                    if c > 0:
                        # check up and to the left
                        if grid[r][c-1] == "^":
                            grid[r][c] += int(grid[r-1][c-1])
                            sum += int(grid[r-1][c-1])
            # print the sum of the numbers in the current row
            print(sum)
    return grid

def sum_row(row):
    sum = 0
    for x in row:
        x = int(x)
        if x > 0:
            sum += int(x)
    return sum

grid = []
file_data = get_file_data("input.txt")

# Create a list to hold the lines
for line in file_data:
    row = []
    for x in line:
        row.append(x)
    grid.append(row)

add_borders(grid)
no_s_grid = replace_s_with_one(grid)
new_grid = part_two(no_s_grid)