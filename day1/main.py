# Set starting frequency
frequency = 0

# Open input file and convert to array
with open('input.txt', 'r') as file:
    calibration_steps = file.read().split('\n')

# Go through each step in calibration steps
for step in calibration_steps:
    # Add the step to the frequency, convert from string to int
    frequency += int(step)

# Report final frequency
print('The final frequency is:')
print(frequency)

twice = False

# Set starting frequency
frequency = 0

# Array to hold previous frequencies
previous_frequencies = [0, ]

while twice is False:
    for step in calibration_steps:
        # Add the step to the frequency, convert from string to int
        frequency += int(step)

        # If frequency has already appeared stop both loops
        if frequency in previous_frequencies:
            twice = frequency
            break

        # Add frequency the list of previously occurrences
        previous_frequencies.append(frequency)

print('')
print('The frequency that reaches twice is:')
print(twice)
