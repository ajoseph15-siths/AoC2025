# FUNCTIONS
# 1. Create a list to hold the contents of the input file
def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        if "x" in line:
            data.append(line.rstrip())
    return data

# 2. Create regions
def create_regions(input_list):
    count = 0
    for region in input_list:
        # get the area of the tree region
        x = region.index("x")
        colon = region.index(":")
        width = int(region[0:x])
        height = int(region[x+1:colon])
        tree_region_area = width * height
        # get the area of the gifts
        num_of_gifts_as_strings = region[colon+1:].strip().split(" ")
        num_of_gifts = []
        for num in num_of_gifts_as_strings:
            num_of_gifts.append(int(num))
        gift_area = sum(num_of_gifts) * 9
        # compare
        if tree_region_area >= gift_area:
            count += 1
    return count

# COMMANDS
# 1. get info from input file
input_list = get_file_data('input.txt')
# 2. run
print(create_regions(input_list))