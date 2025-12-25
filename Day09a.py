from itertools import combinations

# 1. Create a list to hold the contents of the input file
def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

# 2. Create list of x,y tuples
def create_list_of_points(input_list):
    list_of_points = []
    for line in input_list:
        point_as_string = tuple(line.split(','))
        x = int(point_as_string[0])
        y = int(point_as_string[1])
        point = (x, y)
        list_of_points.append(point)
    return list_of_points

# 3. find all combinations of two points
# for each pair, create an object and add it to a list
def add_pairs_to_list(list_of_points):
    all_pairs = []
    # get all combinations of 2 points
    res = list(combinations(list_of_points, 2))
    for i in res:
        point1 = i[0]
        point2 = i[1]
        # calculate area of rectangle created by points
        area = calculate_area(point1, point2)
        pair_of_points = (point1, point2, area)
        all_pairs.append(pair_of_points)
    return all_pairs

# 3a. calculate the area of the rectangle created by a pair of points
def calculate_area(point1,point2):
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    # add 1 to the larger of the x's and y's
    if x1 > x2:
        x1 = x1 + 1
    else:
        x2 = x2 + 1
    if y1 > y2:
        y1 = y1 + 1
    else:
        y2 = y2 + 1
    x_diff = abs(x2 - x1)
    y_diff = abs(y2 - y1)
    return x_diff * y_diff

# 1. get the data from the input file and put into a list
print("Step 1 of 5: Getting data from input file...")
input_list = get_file_data("input.txt")

# 2. each line in the input_list is an x,y coordinate
# convert the line into a TUPLE with x, y coordinates
# add the tuple to the LIST of points
print("Step 2 of 5: Creating x,y tuples...")
list_of_points = create_list_of_points(input_list)

# 3. find all combinations of two points
print("Step 3 of 5: Creating pairs of points and add to list...")
pairs = add_pairs_to_list(list_of_points)

# 4. order the pairs by area
print("Step 4 of 5: Sorting pairs by rectangle area...")
pairs.sort(key=lambda pair: pair[2], reverse=True)

# 5. print the area of the largest rectangle
print("Step 5 of 5: Print the largest rectangle area...")
print("Part 1 Answer:",pairs[0][2])