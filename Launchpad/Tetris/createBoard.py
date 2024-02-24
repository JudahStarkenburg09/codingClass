# Define the size of the array
num_rows = 8
num_cols = 8

# Initialize an empty list to store the array
array_list = []

# Define the numbers list
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 16, 17, 18, 19, 20, 21, 22, 23, 32, 33, 34, 35, 36, 37, 38, 39,
           48, 49, 50, 51, 52, 53, 54, 55, 64, 65, 66, 67, 68, 69, 70, 71, 80, 81, 82, 83, 84, 85,
           86, 87, 96, 97, 98, 99, 100, 101, 102, 103, 112, 113, 114, 115, 116, 117, 118, 119]

# Loop through each row
for i in range(num_rows):
    # Initialize a temporary row list
    row_list = []
    # Loop through each column
    for j in range(num_cols):
        # Calculate the index for the current element
        index = i * num_cols + j
        # Calculate the value based on the pattern
        value = [0, 0, 0]
        array = {numbers[0]:value}
        # Append the value to the temporary row list
        row_list.append(array)
        numbers.remove(numbers[0])
    # Append the temporary row list to the array list
    array_list.append(row_list)

# Print the resulting array list
for row in array_list:
    print(row)

