import cv2
import numpy as np

def mapFunc(n):
    return int(n > 127)

def video_to_frames(video_path, output_json_path):
    cap = cv2.VideoCapture(video_path)

    with open(output_json_path, 'a') as json_file:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Convert the frame to grayscale
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Convert pixel values to binary (black or white)
            _, binary_frame = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_BINARY)

            binary_frame = binary_frame.flatten()
            
        
            data = str(list(map(mapFunc, binary_frame))).replace(" ", "").replace(",","").replace("]","").replace("[","")
            json_file.write(data)

    cap.release()

# Example usage
video_path = './output.mp4'
output_json_path = './frames.txt'
video_to_frames(video_path, output_json_path)

input_json_path = './frames.txt'
output_combined_path = './combined_frames.txt'
segment_size = 150**2

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