input_json_path = './frames.txt'
output_combined_path = './combined_frames.txt'
segment_size = 150**2


with open(input_json_path, 'r') as input_file:
    content = input_file.read()
    input_file.close()

with open(output_combined_path, 'w') as output_file:
    for i in range(0, len(content), 4):
        hex_value = hex(int(content[i:i+4], 2))[2:]
        output_file.write(hex_value)

"""
with open(input_json_path, 'r') as input_file:
    content = input_file.read()

# Calculate the number of segments needed
num_segments = (len(content) + segment_size - 1) // segment_size

# Initialize an empty list to store segments
segments = []

# Split the content into segments
for i in range(num_segments):
    start_idx = i * segment_size
    end_idx = (i + 1) * segment_size
    segment_content = content[start_idx:end_idx]
    segments.append(segment_content)

# Join segments with commas
combined_content = ','.join(segments)

# Write the combined content to a new file
with open(output_combined_path, 'w') as output_file:
    output_file.write(combined_content)
    print(len(combined_content.split(",")))
"""