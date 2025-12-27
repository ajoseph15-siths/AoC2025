from itertools import product, combinations, combinations_with_replacement, permutations

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
        joltage_requirements = line[j:]
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

# 3. for all machines, find the smallest number of button presses to match
# the indicator light diagram, and sum those
def part_one(all_machines):
    total_button_presses = 0
    for machine in all_machines:
        total_button_presses += find_fewest_button_presses(machine)
    print("Part 1: TOTAL button presses for all machines =",total_button_presses)

# 3a. find the maximum button presses for ONE machine
def find_fewest_button_presses(one_machine):
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

# COMMANDS

# 1. get info from input file
input_list = get_file_data('input.txt')

# 2. create machine objects from input file and add to a list
all_machines = create_machines(input_list)

# 3. push the buttons in different combinations for all machines
part_one(all_machines)