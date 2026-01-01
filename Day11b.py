from functools import cache
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
   return tuple(all_devices)
# 3. Find a way out, given a "starting" device
def find_way_out(device_id, all_devices):
    # find connected devices
    count = 0
    connected_devices = tuple([])
    for device in all_devices:
        if device[0] == device_id:
            connected_devices = device[1]
    # loop through the connected devices
    for connected_device in connected_devices:
        if connected_device == "out":
            count += 1
        else:
            count += find_way_out(connected_device, all_devices)
    return count
# 4. Find a way out starting from svr through dac and fft
@cache
def find_way_out_through_dac_fft(device_id, all_devices, dac, fft):
    count = 0
    if device_id == "dac":
        dac = True
    if device_id == "fft":
        fft = True
    # find connected devices
    connected_devices = []
    for device in all_devices:
        if device[0] == device_id:
            connected_devices = device[1]
    # loop through the connected devices
    for connected_device in connected_devices:
        # also need to check if fft and dac have already been visited
        if connected_device == "out" and dac and fft:
            count += 1
        else:
            count += find_way_out_through_dac_fft(connected_device, all_devices, dac, fft)
    return count

# COMMANDS
# 1. get info from input file
input_list = get_file_data('input.txt')
# 2. create devices from input file and add to a list
all_devices = create_devices(input_list)
# 3. find the ways out
#print("Part 1 answer:", find_way_out("you", all_devices))
# 4. find the ways out through fft and dac

print("Part 2 answer:", find_way_out_through_dac_fft("svr", all_devices, False, False))
