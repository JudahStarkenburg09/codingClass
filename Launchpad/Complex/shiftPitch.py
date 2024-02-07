import json
import os

def pitchShift(filename, shift):
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Path to the JSON file
    file_path = os.path.join(current_dir, filename)

    # Read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Loop through each dictionary in the list
    for item in data:
        # Update the "Note" key by adding 12
        item['Note'] += shift

    # Write the updated data back to the JSON file
    with open(file_path, 'w') as file:
        file.write('[\n')
        for i, item in enumerate(data):
            json.dump(item, file)
            if i < len(data) - 1:
                file.write(',\n')
            else:
                file.write('\n')
        file.write(']\n')

# Example usage:
pitchShift('e-guitar.json', 12)
