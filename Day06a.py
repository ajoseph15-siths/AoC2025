# Create a list to hold the contents of the input file
my_list = []

# Open the input file
# Strip any whitespaces from the line
# Append each line to the list myList
def open_file():
    with open("input.txt") as f:
        for x in f:
            my_list.append(x.strip())
open_file()

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
def do_math(problem):
    operator = problem[-1]
    answer = int(problem[0])
    if operator == "*":
        for x in problem[1:-1]:
            answer = answer * int(x)
    else:
        for x in problem[1:-1]:
            answer = answer + int(x)
    return answer

def part_one(problems):
    count = 0
    for problem in problems:
        count += do_math(problem)
    print(count)
    return count

problems = harvest_problems(my_list)
part_one(problems)