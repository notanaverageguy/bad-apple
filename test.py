input_json_path = './frames.txt'
output_combined_path = './combined_frames.txt'
segment_size = (150**2) // 4

print("converting to hex")

with open(input_json_path, 'r') as input_file:
    content = input_file.read()

hex_segments = []

for i in range(0, len(content), 4):
    hex_segments.append(hex(int(content[i:i+4], 2))[2:])

str_result = ''.join(hex_segments)

print("finished converting to hex")
print("adding commas")

segments = []

for i in range(0, len(str_result), segment_size):
    segments.append(str_result[i:i+segment_size])

segments = ','.join(segments)

print("finished commas")
print("writing to file")

with open(output_combined_path, 'w') as output_file:
    output_file.write(segments)

print("finished")