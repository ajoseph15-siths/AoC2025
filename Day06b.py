# Create a list to hold the contents of the input file
my_list = []

# Open the input file
# Strip any whitespaces from the line
# Append each line to the list myList
def open_file():
    with open("input.txt") as f:
        for x in f:
            my_list.append(x.replace("\n",""))
open_file()

# get the indices of the operators
def get_indices(my_list):
    indices = []
    for i,x in enumerate(my_list[-1]):
        if x != " ":
            indices.append(i)
    return indices

# add spaces to the end of any rows that are too short
def get_longest_row_length(my_list):
    length = 0
    for list in my_list:
        if len(list) > length:
            length = len(list)
    return length

# go through each row and add spaces if necessary
def add_space(my_list,length):
    for i,list in enumerate(my_list):
        while len(my_list[i]) < length:
            my_list[i] = my_list[i] + " "
    return my_list

# loop through the indices (which indicate each problem)
# loop through each "column"/character in a row within the problem (between indices)
# then loop through each row to get each digit to create a number
# add each number to a problem list
def harvest_vertical_problems(my_list,indices):
    # a list to hold lists of numbers that belong to the same problem
    problems = []
    # loop through the operators
    for i,index in enumerate(indices):
        # a list to hold numbers that belong to the same problem
        current_problem_numbers = []
        # variable to hold operator when you find it
        operator = ""
        start = index
        # if you're at the last index in indices
        if i == len(indices) - 1:
            # bad hardcoded number; the distance between indices
            # 4 for sample, 5 for my input
            end = index + 5
        else:
            end = indices[i+1]
        # loop through the columns
        for col in range(start,end-1):
            number_in_problem = ""
            # loop through the rows
            for row in my_list:
                if row[col].isdigit():
                    number_in_problem += row[col]
                if row[col] == "*" or row[col] == "+":
                    operator = row[col]
            current_problem_numbers.append(number_in_problem)
        # find the operator and add it to the end of the numbers
        current_problem_numbers.append(operator)
        problems.append(current_problem_numbers)
    return problems

def harvest_problems(my_list):
    problems = []
    # put rows into a list
    problem_rows = []
    # replace spaces with commas in each row
    for row in my_list:
        comma_separated_problem = (','.join(row.split())).split(',')
        problem_rows.append(comma_separated_problem)
    # transpose problems
    # loop through the 1st, 2nd, through nth item in each row (these are like columns)
    # for each row, only get ONE item: the nth item
    # add it to the problem row list
    # then move on to the next column, beginning at row 0 again
    for n in range(len(problem_rows[0])):
        new_problem = []
        for row in problem_rows:
            new_problem.append(row[n])
        problems.append(new_problem)
    return problems

# take in all numbers and operator in the problem (list)
# index -1 = operator
# index 0:-1 = numbers separated by commas
# operate
# return the result
def do_one_math_problem(problem):
    operator = problem[-1]
    answer = int(problem[0])
    if operator == "*":
        for x in problem[1:-1]:
            answer = answer * int(x)
    else:
        for x in problem[1:-1]:
            answer = answer + int(x)
    return answer

def do_the_math(problems):
    count = 0
    for problem in problems:
        count += do_one_math_problem(problem)
    return count

part_one_problems = harvest_problems(my_list)
length = get_longest_row_length(my_list)
add_space(my_list,length)
part_two_problems = harvest_vertical_problems(my_list, get_indices(my_list))

print("part one:",do_the_math(part_one_problems))
print("part two:",do_the_math(part_two_problems))