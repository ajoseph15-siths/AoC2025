# FUNCTIONS
# 1. Create a list to hold the contents of the input file
def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data
# 2. Create devices from each line in the input file
def create_devices(input_list):
   all_devices = []
   for line in input_list:
       i = line.index(':')
       # separate the line into device id: connected devices
       device_id = line[:i]
       connected_devices = tuple(line[i+1:].split())
       all_devices.append((device_id, connected_devices))
   return all_devices
# 3. Find a way out, given a "starting" device
# this doesn't actually work... i had to run it and copy and paste the output
# into notepad++ and then count how many times it printed "found a way out"
def find_way_out(device_id, all_devices, count):
    # find connected devices
    connected_devices = []
    for device in all_devices:
        if device[0] == device_id:
            connected_devices = device[1]
    # loop through the connected devices
    for connected_device in connected_devices:
        if connected_device == "out":
            print("found a way out")
            count += 1
        else:
            find_way_out(connected_device, all_devices, count)
    return count

# COMMANDS
# 1. get info from input file
input_list = get_file_data('input.txt')
# 2. create devices from input file and add to a list
all_devices = create_devices(input_list)
# 3. find the ways out
print(find_way_out("you", all_devices,0))