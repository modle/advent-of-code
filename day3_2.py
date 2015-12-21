import itertools

house = [[0, 0], [0, 0]]
# char_count = 0

with open('day3_input.txt', 'r') as myfile:
    data = myfile.read()

for char in data:
    m = house[len(house)-2]

    print char

    if char == '^':
        house.append([m[0], m[1]+1])
    elif char == 'v':
        house.append([m[0], m[1]-1])
    elif char == '<':
        house.append([m[0]-1, m[1]])
    elif char == '>':
        house.append([m[0]+1, m[1]])

    # char_count += 1

    # if char_count == 10:
    #     break

# print house

house.sort()

h = list(house for house, _ in itertools.groupby(house))

print(len(h))
