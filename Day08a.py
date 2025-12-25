import math
from itertools import combinations

# create objects from each string in the list
class junction_box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def get_info(self):
        return [self.x, self.y, self.z]
    #def __eq__(self, other):
    #    return self.x == other.x and self.y == other.y and self.z == other.z

# create objects from two boxes
class pair_of_boxes:
    def __init__(self,box1,box2):
        self.box1 = box1
        self.box2 = box2
        self.distance = distance_between_two_boxes(box1.x, box1.y, box1.z, box2.x, box2.y, box2.z)
    def __eq__(self, other):
        same_order = self.box1 == other.box1 and self.box2 == other.box2
        different_order = self.box1 == other.box2 and self.box2 == other.box1
        return same_order or different_order
    def get_info(self):
        return f"Distance between {self.box1.get_info()} and {self.box2.get_info()} is {self.distance}"

# Create a list to hold the contents of the input file
def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

# calculate distance between two boxes
def distance_between_two_boxes(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)

# create one junction box from a line of three numbers separated by commas
def create_junction_box(line):
    separated = line.split(",")
    box = junction_box(int(separated[0]), int(separated[1]), int(separated[2]))
    return box

# create a pair of junction boxes from two junction boxes
def create_pair_of_junction_boxes(box1,box2):
    pair = pair_of_boxes(box1, box2)
    #print("Created pair of junction boxes:",pair.get_info())
    return pair

# loop through input data file, create junction boxes,
# and add each to a list
def add_boxes_to_list(input_list):
    all_junction_boxes = []
    for line in input_list:
        box = create_junction_box(line)
        all_junction_boxes.append(box)
    return all_junction_boxes

# loop through all PAIRS of junction boxes (combinations)
# for each pair, create an object and add it to a list
def add_pairs_to_list(all_boxes):
    all_pairs = []
    # get all combinations of 2 boxes
    res = list(combinations(all_boxes, 2))
    for i in res:
        pair = create_pair_of_junction_boxes(i[0],i[1])
        # i is a tuple
        # i[0] is a junction box object
        all_pairs.append(pair)
    return all_pairs

# put each box into its own list
def create_initial_circuits(all_boxes):
    all_initial_circuits = []
    for box in all_boxes:
        all_initial_circuits.append({box})
    return all_initial_circuits

# given a box, find the circuit that it is in
def get_circuit(box, circuits):
    for circuit in circuits:
        if box in circuit:
            #print("Found",box.get_info(),"in circuit:",end=" ")
            #for box in circuit:
            #    print(box.get_info())
            return circuit

# check and join x pairs with shortest distance
def join_circuits(circuits, pair_of_boxes):
    box1 = pair_of_boxes.box1
    box2 = pair_of_boxes.box2
    circuit1 = get_circuit(box1, circuits)
    circuit2 = get_circuit(box2, circuits)
    # union of circuit 1 and circuit 2
    circuit1.update(circuit2)
    # delete circuit 2 from the list of circuits
    # if the circuits are different:
    if circuit1 != circuit2:
        circuits.remove(circuit2)

# join x number of circuits and order the circuits by descending length
def join_x_circuits(number_of_circuits):
    for i in range(number_of_circuits):
        join_circuits(circuits,all_pairs_of_boxes[i])
    # order the circuits by length
    circuits.sort(key=len,reverse=True)
    return circuits

# get x number of circuits' lengths and multiply them
def part_one(circuits, x):
    answer = 1
    for i in range(x):
        answer *= len(circuits[i])
    print("Part 1 Answer:",answer)
    return answer

# get the data from the input file and put into a list
print("Step 1 of 7: Getting data from input file...")
input_list = get_file_data("input.txt")

# test making boxes from input file
print("Step 2 of 7: Making box objects from input file...")
all_boxes = add_boxes_to_list(input_list)

# test making pairs of boxes from list of all boxes
print("Step 3 of 7: Making all pairs of boxes...")
all_pairs_of_boxes = add_pairs_to_list(all_boxes)

# sort the pairs by distance
print("Step 4 of 7: Sorting all pairs of boxes...")
all_pairs_of_boxes.sort(key=lambda pair: pair.distance, reverse=False)

# put each box into its own list
print("Step 5 of 7: Making initial circuits from all boxes...")
circuits = create_initial_circuits(all_boxes)

print("Step 6 of 7: Joining circuits...")
join_x_circuits(1000)

print("Step 7 of 7: Calculating answer...")
part_one(circuits,3)



'''
# test making one pair of boxes
box1 = all_boxes[0]
box2 = all_boxes[1]
box3 = all_boxes[2]
all_pairs = []
pair1_2 = create_pair_of_junction_boxes(box1,box2)
pair2_3 = create_pair_of_junction_boxes(box2,box3)
pair1_3 = create_pair_of_junction_boxes(box1,box3)
all_pairs.append(pair1_2)
all_pairs.append(pair2_3)
all_pairs.append(pair1_3)

# test getting a circuit that contains a specified box
#for box in all_boxes:
#    get_circuit(box, circuits)

# test joining circuits in three test pairs
#for pair in all_pairs:
#    join_circuits(circuits, pair)

# check types of things in circuits
for circuit in circuits:
    print("circuits is",type(circuits))
    for circuit in circuits:
        print("circuit",circuit,"is",type(circuit))
    for c in circuit:
        print("c",c.get_info(),"in circuit is",type(c))

# check types of things in all_pairs_of_boxes
for pair in all_pairs_of_boxes:
    print("pair",pair.get_info(),"is type",type(pair))
    print("box1",pair.box1.get_info(),"is type",type(pair.box1))
'''