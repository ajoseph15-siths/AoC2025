from itertools import product
from z3 import *

# CLASSES

# create objects from each string in the list
class Machine:
    def __init__(self, indicator_light_diagram, button_wiring_schematic, joltage_requirements):
        self.indicator_light_diagram = indicator_light_diagram
        self.button_wiring_schematic = button_wiring_schematic
        self.joltage_requirements = joltage_requirements
    def get_info(self):
        return [self.indicator_light_diagram, self.button_wiring_schematic, self.joltage_requirements]

# FUNCTIONS

# 1. Create a list to hold the contents of the input file
def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

# 2. create a machine object from each line in the input file
def create_machines(input_list):
   all_machines = []
   for line in input_list:
       i = line.index(']')
       j = line.index('{')
       # separate the line into lights, buttons, and joltages
       indicator_light_diagram = convert_indicator_light_diagram(line[1:i])
       button_wiring_schematic = convert_button_wiring_schematic(line[i+2:j-1])
       joltage_requirements = convert_joltage_requirements(line[j+1:-1])
       # make the machine
       machine = Machine(indicator_light_diagram, button_wiring_schematic, joltage_requirements)
       #print("Adding machine:",machine.get_info())
       all_machines.append(machine)
   return all_machines

# 2a. convert indicator_light_diagram as a string into a list of booleans
def convert_indicator_light_diagram(indicator_light_diagram):
   ild_split = list(indicator_light_diagram)
   ild_as_booleans = []
   for i in ild_split:
       if i == '.':
           ild_as_booleans.append(False)
       else:
           ild_as_booleans.append(True)
   return ild_as_booleans

# 2b. convert button_wiring_schematic as a string into a list of tuples
def convert_button_wiring_schematic(button_wiring_schematic):
   bws_split = button_wiring_schematic.split()
   bws_as_tuples = []
   for i in bws_split:
       i_no_parentheses = i[1:-1]
       bws = i_no_parentheses.split(',')
       bws_as_ints = []
       for b in bws:
           bws_as_ints.append(int(b))
       bws_as_tuples.append(bws_as_ints)
   return bws_as_tuples

# 2c. convert joltage_requirements as a string into list of integers
def convert_joltage_requirements(joltage_requirements):
   jrs_split = joltage_requirements.split(",")
   jrs_as_ints = []
   for jr in jrs_split:
       jrs_as_ints.append(int(jr))
   return jrs_as_ints

# 3. for all machines, find the smallest number of button presses to match
# the indicator light diagram, and sum those
def part_one(all_machines):
    total_button_presses = 0
    for machine in all_machines:
        total_button_presses += find_fewest_button_presses_for_lights(machine)
    print("Part 1: TOTAL button presses for all machines =",total_button_presses)

# 3a. find the maximum button presses for ONE machine
def find_fewest_button_presses_for_lights(one_machine):
    # make an "OFF" indicator light diagram
    fresh_ild = make_fresh_ild(len(one_machine.indicator_light_diagram))
    target_ild = one_machine.indicator_light_diagram
    max_button_presses = 1
    while fresh_ild != target_ild:
        # while your target ILD has not been met, press buttons
        button_combinations = button_combos(one_machine.button_wiring_schematic, max_button_presses)
        for combo in button_combinations:
            fresh_ild = make_fresh_ild(len(one_machine.indicator_light_diagram))
            for c in combo:
                fresh_ild = push_button(fresh_ild, c)
                if fresh_ild == target_ild:
                    return max_button_presses
        max_button_presses += 1
    return max_button_presses

# 3b. create a fresh OFF indicator light diagram
def make_fresh_ild(ild_length):
    fresh_ild = []
    for i in range(ild_length):
        fresh_ild.append(False)
    return fresh_ild

# 3c. generate all combinations of button presses given a list of buttons
# and the maximum number of buttons that can be pressed
# 1st arg: p is the list of buttons you could press
# 2nd arg: repeat is the max number of button presses
def button_combos(list_of_buttons, max_number_of_button_presses):
    return product(list_of_buttons,repeat=max_number_of_button_presses)

# 3d. push a button
# input: indicator light diagram (string), one schematic from a bws (tuple)
def push_button(indicator_light_diagram, one_schematic):
    for i,scheme in enumerate(one_schematic):
        if indicator_light_diagram[one_schematic[i]]:
            (indicator_light_diagram[one_schematic[i]]) = False
        else:
            (indicator_light_diagram[one_schematic[i]]) = True
    return indicator_light_diagram

# 4. for all machines, find the smallest number of button presses to match
# the joltages, and sum those
def part_two(all_machines):
    total_button_presses = 0
    for machine in all_machines:
        total_button_presses += find_fewest_button_presses_for_joltages(machine)
    print("Part 2: TOTAL button presses for all machines =",total_button_presses)

# 4a. find_fewest_button_presses_for_joltages
def find_fewest_button_presses_for_joltages(one_machine):
    coefficient_matrix = create_coefficient_matrix(one_machine)
    return solve_system_of_equations(coefficient_matrix,one_machine.joltage_requirements)

# 4b. solve system of equations
def solve_system_of_equations(coefficient_matrix, results_matrix):
    optimizer = Optimize()
    # the variables, one for each button
    variables = []
    for i in range(len(coefficient_matrix[0])):
        i = Int(i)
        variables.append(i)
    '''
    a, b, c, d, e, f = Ints('a b c d e f')
    '''
    # add the condition that the variables must be positive
    for variable in variables:
        optimizer.add(variable >= 0)
    '''
    optimizer.add(a >= 0)
    optimizer.add(b >= 0)
    optimizer.add(c >= 0)
    optimizer.add(d >= 0)
    optimizer.add(e >= 0)
    optimizer.add(f >= 0)
    '''
    # add the equations
    # loop through the joltage/results matrix
    # for each joltage, look at its corresponding row in the coefficient matrix
    # joltage = corresponding row in coefficient matrix
    for j,joltage in enumerate(results_matrix):
        # j is the index of the joltage and its corresponding coefficient matrix
        variables_in_equation = []
        for c,coefficient in enumerate(coefficient_matrix[j]):
            if coefficient == 1:
                variables_in_equation.append(variables[c])
        optimizer.add(sum(variables_in_equation) == joltage)
    '''
    optimizer.add(e + f == 3)
    optimizer.add(b + f == 5)
    optimizer.add(c + d + e == 4)
    optimizer.add(a + b + d == 7)
    '''
    # save the result of the minimum number of total button presses
    result = optimizer.minimize(sum(variables))
    '''
    result = optimizer.minimize(a + b + c + d + e + f)
    '''
    # if there is a solution and all conditions are satisfiable
    if optimizer.check() == sat:
        # print the values of each variable
        # print(optimizer.model())  # [d = 1, a = 1, e = 3, b = 5, f = 0, c = 0]
        # print the total number of button presses
        # print(result.value().as_long())
        return result.value().as_long()
    return 0

# 4c. given a machine, create its coefficient matrix and results matrix
def create_coefficient_matrix(one_machine):
    buttons = one_machine.button_wiring_schematic
    joltages = one_machine.joltage_requirements
    # create a new list to hold the coefficient matrix
    coefficient_matrix = []
    # create a new list to hold the coefficients for one button
    # fill it with 0's; it should be the length of the joltages list
    for i in range(len(joltages)):
        row_with_zeros = [0] * len(buttons)
        coefficient_matrix.append(row_with_zeros)
    # loop through each row (equation/joltage) in the coefficient matrix
    # each item in the row corresponds to one of the buttons
    # loop through each button
    # if the button the corresponds to the item in the row contains that row index
    # change from a 0 to a 1
    for i,equation in enumerate(coefficient_matrix):
        for j,item in enumerate(equation):
            if i in buttons[j]:
                coefficient_matrix[i][j] = 1
    return coefficient_matrix

# COMMANDS

# 1. get info from input file
input_list = get_file_data('input.txt')

# 2. create machine objects from input file and add to a list
all_machines = create_machines(input_list)

# 3. push the buttons in different combinations for all machines
part_one(all_machines)
part_two(all_machines)