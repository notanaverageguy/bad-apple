import cv2
import numpy as np

def mapFunc(n):
    return int(n > 127)

def video_to_frames(video_path, output_json_path):
    cap = cv2.VideoCapture(video_path)

    with open(output_json_path, 'w') as json_file:
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
