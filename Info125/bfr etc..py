import math

# size calculation/input data
block_size = 1040
gap_size = 124
blocks_per_track = 20
tracks_per_surface = 400
disk_pack = (15 * 2)
disk_rotation = 2400
cylinder = tracks_per_surface  # Number of Cylinders is the same as the number of tracks per surface
total_capacity = (block_size + gap_size) * blocks_per_track
useful_capacity = block_size * blocks_per_track

# rotation speed input data
seek_time = 30
rotation_delay = 12.5
block_transfer = 1
random_blocks = 20
total_transfer_rate = ttr = total_capacity / (60 * 1000 / disk_rotation)
bulk_transfer_rate = btr = (block_size / (block_size + gap_size)) * ttr
disk_access_time = seek_time + rotation_delay + block_transfer

# record input data
record = 40
number_of_records = 14300

# prints and calculates various data based on the previous input data
print("Total, and useful capacity:")
print(total_capacity, useful_capacity)

total_cylinder_capacity = disk_pack * blocks_per_track * (block_size + gap_size)
useful_cylinder_capacity = disk_pack * blocks_per_track * block_size
print("Total, and useful cylinder capacity:")
print(total_cylinder_capacity, useful_cylinder_capacity)

total_disk_pack_capacity = total_cylinder_capacity * tracks_per_surface
useful_disk_pack_capacity = useful_cylinder_capacity * tracks_per_surface
print("Total, and useful disk pack capacity in MB:")
print(math.floor(total_disk_pack_capacity / (2 ** 20)), math.floor(useful_disk_pack_capacity / (2 ** 20)))

print("Disk access time")
print(disk_access_time)

print("Time to access 20 random blocks:")
print(disk_access_time * random_blocks)

print("Time to access 20 consecutive blocks:")
print(seek_time + rotation_delay + (random_blocks * (block_size / btr)))

# Record that can fit within a block/calculates bfr
blocking_factor = bfr = math.floor(block_size / record)
required_blocks = number_of_records / bfr
linear_search = math.floor(required_blocks / 2)

print("block factor bfr/records per block")
print(bfr)
print("Total required blocks:")
print(math.floor(number_of_records / bfr))
print("Wasted space per block in bytes:")
print(block_size - (record * bfr))
print("Average number of block accesses needed to search for an arbitrary record:")
print(linear_search)
print("Linear search, consecutive and double buffer:")
print(seek_time + rotation_delay + (linear_search * (block_size / btr)))
print("Linear search, but blocks are not stored consecutively:")
print(linear_search * disk_access_time)
