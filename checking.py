input_file_path = './combined_frames.txt'
desired_character = ','  # Replace with the character you want to count

# Open the file in read mode
with open(input_file_path, 'r') as input_file:
    # Read the content of the file
    content = input_file.read()

# Count occurrences of the desired character
count = content.count(desired_character)

print(f"The character '{desired_character}' appears {count} times in the file.")