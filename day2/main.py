from collections import Counter

with open('input.txt', 'r') as file:
    box_ids = file.read().split('\n')


threes = 0
twos = 0

for box_id in box_ids:
    # Count the same letters
    counter = Counter(list(box_id))
    two = three = False

    # Loop through each letter counter
    for count in counter:
        two = (counter[count] is 2) or two  # If a letter appears twice
        three = (counter[count] is 3) or three  # If a letter appears thrice

    twos += 1 if two else 0  # Add to twos counter if a letter appeared twice
    threes += 1 if three else 0  # Add to threes counter if a latter appeared thrice

print('The checksum for the box IDs are:')
print(twos * threes)

sames = []

# Double for loop to compare each item in the list with one another
for box_id1 in box_ids:
    for box_id2 in box_ids:

        # If the two IDs are the same skip
        if box_id1 is box_id2:
            continue

        similar_chars = 0

        # Loop through each character in the IDs and compare if they are the same
        for i in range(len(box_id1)):
            similar_chars += 1 if box_id1[i] is box_id2[i] else 0

        # Check if there is only 1 different character
        if len(box_id1) - similar_chars == 1:
            sames = [box_id1, box_id2]
            break

print('')
print('The two same ids are ' + sames[0] + ' and ' + sames[1])
common_letters = ''

# Loop over the two ids to and remove the unlike character
for i in range(len(sames[0])):
    common_letters += sames[0][i] if sames[0][i] is sames[1][i] else ''

print('The common letters are :')
print(common_letters)
