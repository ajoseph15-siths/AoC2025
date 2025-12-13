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
        grid[-1].append(".")
    return grid

# replace S with |
def replace_s_with_pipe(grid):
    for r,row in enumerate(grid):
        for c,col in enumerate(row):
            if grid[r][c] == "S":
                grid[r][c] = "|"
    return grid

# split
# make a counter
# take two rows. check the first row for S or |
# if found, check same column in row below for ^
# if found, add | to left and right of the column. add one to the counter.
# else, add | to column
# go to the next row
count = 0

def part_one(grid, count):
    for r,row in enumerate(grid):
        if r < len(grid)-2:
            if "|" in row:
                for c,col in enumerate(row):
                    if grid[r][c] == "|":
                        # look below
                        below = grid[r+1][c]
                        if below == "^":
                            count += 1
                            print("^ is below")
                            # split
                            grid[r+1][c-1] = "|"
                            grid[r+1][c+1] = "|"
                        else:
                            grid[r+1][c] = "|"
    print_grid(grid)
    print("Part one:", count)
    return grid

grid = []
file_data = get_file_data("input.txt")

# Create a list to hold the lines
for line in file_data:
    row = []
    for x in line:
        row.append(x)
    grid.append(row)

add_borders(grid)
no_s_grid = replace_s_with_pipe(grid)
new_grid = part_one(no_s_grid,count)